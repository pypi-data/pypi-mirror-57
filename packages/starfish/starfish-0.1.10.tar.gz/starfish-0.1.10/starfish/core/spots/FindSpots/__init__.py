from ._base import FindSpotsAlgorithm
from .blob import BlobDetector
from .local_max_peak_finder import LocalMaxPeakFinder
from .trackpy_local_max_peak_finder import TrackpyLocalMaxPeakFinder

# autodoc's automodule directive only captures the modules explicitly listed in __all__.
all_filters = {
    filter_name: filter_cls
    for filter_name, filter_cls in locals().items()
    if isinstance(filter_cls, type) and issubclass(filter_cls, FindSpotsAlgorithm)
}
__all__ = list(all_filters.keys())
