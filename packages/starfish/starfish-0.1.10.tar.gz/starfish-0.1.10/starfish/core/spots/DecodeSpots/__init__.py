from ._base import DecodeSpotsAlgorithm
from .metric_decoder import MetricDistance
from .per_round_max_channel_decoder import PerRoundMaxChannel
from .simple_lookup_decoder import SimpleLookupDecoder

# autodoc's automodule directive only captures the modules explicitly listed in __all__.
all_filters = {
    filter_name: filter_cls
    for filter_name, filter_cls in locals().items()
    if isinstance(filter_cls, type) and issubclass(filter_cls, DecodeSpotsAlgorithm)
}
__all__ = list(all_filters.keys())
