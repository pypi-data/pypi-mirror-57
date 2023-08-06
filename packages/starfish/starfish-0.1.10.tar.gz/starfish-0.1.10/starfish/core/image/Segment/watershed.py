from typing import Mapping, Optional, Tuple

import numpy as np
import scipy.ndimage.measurements as spm
from scipy.ndimage import distance_transform_edt
from showit import image
from skimage.feature import peak_local_max
from skimage.morphology import disk, watershed

from starfish.core.image.Filter import Reduce
from starfish.core.image.Filter.util import bin_open
from starfish.core.imagestack.imagestack import ImageStack
from starfish.core.morphology import Filter
from starfish.core.morphology.Binarize import ThresholdBinarize
from starfish.core.morphology.binary_mask import BinaryMaskCollection
from starfish.core.types import ArrayLike, Axes, Coordinates, FunctionSource, Levels, Number
from ._base import SegmentAlgorithm


class Watershed(SegmentAlgorithm):
    """
    Implements watershed segmentation of cells.

    Algorithm is seeded by nuclei image. Binary segmentation mask is computed from a maximum
    projection of spots across C and R, which is subsequently thresholded.

    This function wraps :py:func:`skimage.morphology.watershed`

    Parameters
    ----------
    nuclei_threshold : Number
        threshold to apply to nuclei image
    input_threshold : Number
        threshold to apply to stain image
    min_distance : int
        minimum distance before object centers in a provided nuclei image are considered single
        nuclei

    Notes
    -----
    Watershed: http://scikit-image.org/docs/dev/auto_examples/segmentation/plot_watershed.html

    """

    def __init__(
        self,
        nuclei_threshold: Number,
        input_threshold: Number,
        min_distance: int,
    ) -> None:

        self.nuclei_threshold = nuclei_threshold
        self.input_threshold = input_threshold
        self.min_distance = min_distance
        self._segmentation_instance: Optional[_WatershedSegmenter] = None

    def run(
            self,
            primary_images: ImageStack,
            nuclei: ImageStack,
            *args
    ) -> BinaryMaskCollection:
        """Segments nuclei in 2-d using a nuclei ImageStack

        Primary images are used to expand the nuclear mask, but only in cases where there are
        densely detected points surrounding the nuclei.

        Parameters
        ----------
        primary_images : ImageStack
            contains primary image data
        nuclei : ImageStack
            contains nuclei image data

        Returns
        -------
        masks : BinaryMaskCollection
           binary masks segmenting each cell
        """

        # create a 'stain' for segmentation
        mp = primary_images.reduce({Axes.CH, Axes.ZPLANE}, func="max")
        mean = Reduce(
            dims=(Axes.ROUND,),
            func="mean",
            level_method=Levels.SCALE_BY_IMAGE).run(mp)
        stain = mean._squeezed_numpy(Axes.ROUND, Axes.CH, Axes.ZPLANE)

        # TODO make these parameterizable or determine whether they are useful or not
        size_lim = (10, 10000)
        disk_size_markers = None
        disk_size_mask = None

        self._segmentation_instance = _WatershedSegmenter(nuclei, stain)
        label_image_array = self._segmentation_instance.segment(
            self.nuclei_threshold, self.input_threshold, size_lim, disk_size_markers,
            disk_size_mask, self.min_distance
        )

        # we max-projected and squeezed the Z-plane so label_image.ndim == 2
        physical_ticks: Mapping[Coordinates, ArrayLike[Number]] = {
            coord: nuclei.xarray.coords[coord.value].data
            for coord in (Coordinates.Y, Coordinates.X)
        }

        return BinaryMaskCollection.from_label_array_and_ticks(
            label_image_array,
            None,
            physical_ticks,
            None,  # TODO: (ttung) this should really be logged.
        )

    def show(self, figsize: Tuple[int, int]=(10, 10)) -> None:
        if isinstance(self._segmentation_instance, _WatershedSegmenter):
            self._segmentation_instance.show(figsize=figsize)
        else:
            raise RuntimeError('Run segmentation before attempting to show results.')


class _WatershedSegmenter:
    def __init__(self, nuclei: ImageStack, stain_img: np.ndarray) -> None:
        """Implements watershed segmentation of cells seeded from a nuclei image

        Algorithm is seeded by a nuclei image. Binary segmentation mask is computed from a maximum
        projection of spots across C and R, which is subsequently thresholded.

        Parameters
        ----------
        nuclei : ImageStack
            nuclei image
        stain_img : np.ndarray[np.float32]
            stain image
        """
        max_project_and_scale = Reduce(
            {Axes.ROUND, Axes.CH, Axes.ZPLANE},
            func="max",
            level_method=Levels.SCALE_BY_IMAGE,
        )
        self.nuclei_mp_scaled = max_project_and_scale.run(nuclei)
        self.stain = stain_img / stain_img.max()

        self.nuclei_thresholded: Optional[np.ndarray] = None  # dtype: bool
        self.markers = None
        self.num_cells: Optional[int] = None
        self.mask = None
        self.segmented = None

    def segment(
            self,
            nuclei_thresh: Number,
            stain_thresh: Number,
            size_lim: Tuple[int, int],
            disk_size_markers: Optional[int]=None,  # TODO ambrosejcarr what is this doing?
            disk_size_mask: Optional[int]=None,  # TODO ambrosejcarr what is this doing?
            min_dist: Optional[Number]=None
    ) -> np.ndarray:
        """Execute watershed cell segmentation.

        Parameters
        ----------
        nuclei_thresh, stain_thresh : Number
            Threshold for the nuclei and stain images. All pixels with intensities above this size
            will be considered part of the objects in the respective images
        size_lim : Tuple[int, int]
            min and max allowable size for nuclei objects in the nuclei_image
        disk_size_markers : Optional[int]
            if provided ...
        disk_size_mask : Optional[int]
            if provided ...
        min_dist : Optional[int]
            if provided, nuclei within this distance of each other are combined into single
            objects.

        Returns
        -------
        np.ndarray[int32] :
            label image with same size and shape as self.nuclei_img
        """
        min_allowed_size, max_allowed_size = size_lim
        self.binarized_nuclei = self.filter_nuclei(nuclei_thresh, disk_size_markers)
        self.markers, self.num_cells = self.label_nuclei(
            self.binarized_nuclei,
            min_allowed_size, max_allowed_size, min_dist
        )
        self.mask = self.watershed_mask(stain_thresh, self.markers, disk_size_mask)
        self.segmented = self.watershed(self.markers, self.mask)
        return self.segmented

    def filter_nuclei(self, nuclei_thresh: float, disk_size: Optional[int]) -> BinaryMaskCollection:
        """Binarize the nuclei image using a thresholded binarizer and perform morphological binary
        opening.

        Parameters
        ----------
        nuclei_thresh : float
            Threshold the nuclei image at this value
        disk_size : int
            if passed, execute a binary opening of the filtered image

        Returns
        -------
        BinaryMaskCollection :
            mask collection with one mask, which is
        """
        nuclei_binarized = ThresholdBinarize(nuclei_thresh).run(self.nuclei_mp_scaled)
        if disk_size is not None:
            disk_img = disk(disk_size)
            nuclei_binarized = Filter.Map(
                "morphology.binary_open",
                disk_img,
                module=FunctionSource.skimage
            ).run(nuclei_binarized)

        # should only produce one binary mask.
        assert len(nuclei_binarized) == 1
        return nuclei_binarized

    def label_nuclei(
        self,
        binarized_nuclei: BinaryMaskCollection,
        min_allowed_size: int,
        max_allowed_size: int,
        min_dist: Optional[Number]=None
    ) -> Tuple[np.ndarray, int]:
        """Construct a labeled nuclei image, which will be combined with the point cloud to seed
        the watershed

        Parameters
        ----------
        binarized_nuclei : BinaryMaskCollection
            BinaryMaskCollection with a single mask, containing the binarized nuclei image
        min_allowed_size : int
            minimum allowable thresholded nuclei size
        max_allowed_size : int
            maximum allowable nuclei size

        Returns
        -------
        np.ndarray :
            labeled nuclei, excluding those whose size is outside the area boundaries

        """
        binarized_nuclei_mask = binarized_nuclei.uncropped_mask(0).values.squeeze(axis=0)

        # label thresholded nuclei image
        if min_dist is None:
            markers, num_objs = spm.label(binarized_nuclei_mask)
        else:
            markers, num_objs = self._unclump(min_dist)

        # TODO dganguli: does it really make sense to assume a square area?
        min_allowed_area = min_allowed_size ** 2
        max_allowed_area = max_allowed_size ** 2

        # spm.sum sums the values of an array by label. This counts the pixels in each object
        areas = spm.sum(
            np.ones(binarized_nuclei_mask.shape),
            markers,
            np.array(range(0, num_objs + 1), dtype=np.int32)
        )

        # each label value is replaced by its area
        area_image = areas[markers]

        # areas are used to mask values that are outside the allowable sizes
        markers[area_image <= min_allowed_area] = 0
        markers[area_image >= max_allowed_area] = 0

        # re-label the image with sequential integers, accounting for exclusion based on size
        markers_reduced, num_objs = self.relabel_image(markers)

        return markers_reduced, num_objs

    def _unclump(self, min_dist: Number) -> Tuple[np.ndarray, int]:
        """
        Run watershed on the thresholded basin image, restricted to basins at least min_dist apart

        Functionally, this reproduces the thresholded nuclei image with overlapping nuclei merged.

        Parameters
        ----------
        min_dist : int
            minimum distance between watershed basins

        """
        im: np.ndarray = self.binarized_nuclei.uncropped_mask(0).values.squeeze(axis=0)

        # calculates the distance of every pixel to the nearest background (0) point
        distance: np.ndarray = distance_transform_edt(im)  # dtype: np.float64

        # boolean array marking local maxima, excluding any maxima within min_dist
        local_maxi: np.ndarray = peak_local_max(
            distance, labels=im, indices=False, min_distance=min_dist
        )

        # label the maxima for watershed
        markers, num_objs = spm.label(local_maxi)

        # run watershed, using the distances in the thresholded image as basins.
        # Uses the original image as a mask, preventing any background pixels from being labeled
        labels_ws: np.ndarray = watershed(-distance, markers, mask=im)
        return labels_ws, num_objs

    def watershed_mask(self, stain_thresh: Number, markers: np.ndarray, disk_size: Optional[int]):
        """Create a watershed mask that is the union of the spot intensities above stain_thresh and
        a marker image generated from nuclei

        Parameters
        ----------
        stain_thresh : Number
            threshold to apply to the stain image
        markers : np.ndarray[bool]
            markers for the stain_image
        disk_size : Optional[int]
            if provided, execute a morphological opening operation over the thresholded stain image

        Returns
        -------
        np.ndarray[bool] :
            thresholded stain image

        """
        st = self.stain >= stain_thresh
        watershed_mask: np.ndarray = np.logical_or(st, markers > 0)  # dtype bool
        if disk_size is not None:
            watershed_mask = bin_open(watershed_mask, disk_size)
        return watershed_mask

    def watershed(self, markers: np.ndarray, watershed_mask: np.ndarray) -> np.ndarray:
        """Run watershed on the thresholded primary_images max projection

        Parameters
        ----------
        markers : np.ndarray[np.int64]
            an array marking the basins with the values to be assigned in the label matrix.
            Zero means not a marker.
        watershed_mask : np.ndarray[bool]
            Mask array. only points at which mask == True will be labeled in the output.

        Returns
        -------
        np.ndarray[np.int32] :
            labeled image, each segment has a unique integer value
        """
        img = 1 - self.stain

        res = watershed(image=img,
                        markers=markers,
                        connectivity=np.ones((3, 3), bool),
                        mask=watershed_mask
                        )

        return res

    @staticmethod
    def relabel_image(image: np.ndarray) -> np.ndarray:
        """given a label image where some objects have been removed, relabel it with sequential integers

        Parameters
        ----------
        image : np.ndarray[np.uint32]
            image whose values identify which object each pixel corresponds to. the values may
            not be sequential integers.

        Returns
        -------
        image : np.ndarray[np.uint32]
            same as input, but the values are re-labled as sequential integers
        num_labels : int
            number of unique objects
        """
        output = np.empty_like(image)
        for i, v in enumerate(np.unique(image)):
            output[np.where(image == v)] = i
        return output, i

    def show(self, figsize=(10, 10)):
        import matplotlib.pyplot as plt
        plt.figure(figsize=figsize)

        plt.subplot(321)
        nuclei_numpy = self.nuclei_mp_scaled._squeezed_numpy(Axes.ROUND, Axes.CH, Axes.ZPLANE)
        image(nuclei_numpy, ax=plt.gca(), size=20, bar=True)
        plt.title('Nuclei')

        plt.subplot(322)
        image(self.stain, ax=plt.gca(), size=20, bar=True)
        plt.title('Stain')

        plt.subplot(323)
        image(
            self.binarized_nuclei.uncropped_mask(0).values.squeeze(axis=0),
            bar=False,
            ax=plt.gca())
        plt.title('Nuclei Thresholded')

        plt.subplot(324)
        image(self.mask, bar=False, ax=plt.gca())
        plt.title('Watershed Mask')

        plt.subplot(325)
        image(self.markers, size=20, cmap=plt.cm.nipy_spectral, ax=plt.gca())
        plt.title('Found: {} cells'.format(self.num_cells))

        plt.subplot(326)
        image(self.segmented, size=20, cmap=plt.cm.nipy_spectral, ax=plt.gca())
        plt.title('Segmented Cells')

        return plt.gca()
