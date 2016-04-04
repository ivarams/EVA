"""!
Collection of all adapters, for easy access when configuring EVA.

_DO NOT_ import anything from here when subclassing adapters!
"""

from eva.base.adapter import BaseAdapter
from eva.adapter.complete import CompleteAdapter
from eva.adapter.delete import DeleteAdapter
from eva.adapter.download import DownloadAdapter
from eva.adapter.fimex import FimexAdapter
from eva.adapter.fimex_grib_to_netcdf import FimexGRIB2NetCDFAdapter
from eva.adapter.null import NullAdapter
from eva.adapter.test_executor import TestExecutorAdapter
