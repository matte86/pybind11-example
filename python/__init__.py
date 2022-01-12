from pkg_resources import get_distribution

from .hello_py import *

__version__ = get_distribution('hello_py').version
