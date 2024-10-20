# Licensed under the MIT License.
# pytypex Copyright (C) 2022 numlinka.

# internal
from . import constants
from .basic import *
from .dirstruct import *


__name__ = "typex"
__author__ = "numlinka"
__license__ = "MIT"
__copyright__ = "Copyright (C) 2022 numlinka"

__version_info__ = (0, 3, 0)
__version__ = ".".join(map(str, __version_info__))


__all__ = [
    "Static",
    "Abstract",
    "abstractmethod",
    "Singleton",
    "Multiton",
    "Atomic",
    "AbsoluteAtomic",
    "MultitonAtomic",

    "FilePath",
    "DirectoryPath",
    "FinalFilePath",
    "FinalDirectoryPath",
    "Directory"
]
