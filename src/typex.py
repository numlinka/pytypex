# Licensed under the MIT License.
# pytypex Copyright (C) 2022 numlinka.

# std
import sys

from abc import ABC, abstractmethod
from types import MethodType
from typing import Dict, Any
from threading import RLock

if sys.version_info >= (3, 11):
    from typing import Self

else:
    from typing import TypeVar
    Self = TypeVar("Self")


__name__ = "typex"
__author__ = "numlinka"
__license__ = "MIT"
__copyright__ = "Copyright (C) 2022 numlinka"

__version_info__ = (0, 2, 0)
__version__ = ".".join(map(str, __version_info__))


DEFAULT = "default"


class Static (object):
    """
    Static class.

    This class cannot be instantiated.
    """
    def __new__(cls):
        raise TypeError("Cannot instantiate static class.")


class Abstract (ABC):
    """
    Abstract class.

    All methods decorated with `abstractmethod` must be rewritten, otherwise they cannot be instantiated.
    """


class Singleton (object):
    """
    Singleton class.

    This class will only be instantiated once to ensure that there is only one instance.
    The `__init__` method of the subclass will be replaced to ensure that the method is only executed once.
    """
    _singleton_instance: Self  # <-- cls
    _singleton_init_method: MethodType  # <-- cls
    _singleton_initialized: bool  # <-- cls

    def __new__(cls, *args, **kwargs) -> Self:
        if cls is Singleton:
            raise TypeError("Cannot instantiate base singleton class.")
        if not hasattr(cls, "_singleton_instance"):
            # In fact, we can directly call the instance's __init__ method in the __new__ phase,
            # and then replace __init__ with an empty function, which can save a lot of things.
            # But I think this is not in line with the norms.
            cls._singleton_init_method = cls.__init__
            cls.__init__ = Singleton.__init__
            cls._singleton_instance = super(Singleton, cls).__new__(cls)
        return cls._singleton_instance

    def __init__(self, *args, **kwargs) -> None:
        cls = self.__class__
        if not hasattr(cls, "_singleton_initialized") or not cls._singleton_initialized:
            cls._singleton_initialized = True
            self._singleton_init_method(*args, **kwargs)


class Multiton (object):
    """
    Multiton pattern class.

    This class can have multiple instances at the same time, and you can create or get them.
    The `__init__` method of the subclass will be replaced to ensure that the method
    is only executed once for each instance.
    """
    _multiton_instances: Dict[str, Self]  # <-- cls
    _multiton_init_method: MethodType  # <-- cls
    _multiton_initialized: bool  # <-- instance
    instance_name: str  # <-- instance

    def __new__(cls, *args, instance_name: str = DEFAULT, **kwargs) -> Self:
        if cls is Multiton:
            raise TypeError("Cannot instantiate base multiton class.")

        if not hasattr(cls, "_multiton_instances"):
            cls._multiton_instances = dict()

        if instance_name in cls._multiton_instances:
            return cls._multiton_instances[instance_name]

        if not hasattr(cls, "_multiton_init_method"):
            cls._multiton_init_method = cls.__init__
            cls.__init__ = Multiton.__init__

        instance = super(Multiton, cls).__new__(cls)

        cls._multiton_instances[instance_name] = instance
        return instance

    def __init__(self, *args, instance_name: str = DEFAULT, **kwargs) -> None:
        self.__instance_name = instance_name
        if not hasattr(self, "_multiton_initialized") or not self._multiton_initialized:
            self._multiton_initialized = True
            self._multiton_init_method(*args, **kwargs)

    @property
    def instance_name(self) -> str:
        """The name of the instance. | **read-only**"""
        return self.__instance_name

    @classmethod
    def get_instance(cls, instance_name: str, *args: Any, **kwargs: Any) -> Self:
        """
        Get an instance of the class.

        Arguments:
            instance_name (str): The name of the instance.
            *args (Any): The arguments to pass to the constructor.
            **kwargs (Any): The keyword arguments to pass to the constructor.
        """
        return cls(*args, instance_name=instance_name, **kwargs)


class Atomic (object):
    """
    Atomic counter.
    """

    def __init__(self):
        self.__lock = RLock()
        self.__count = -1

    def get_count(self) -> int:
        with self.__lock:
            self.__count += 1
            return self.__count

    @property
    def count(self) -> int:
        return self.get_count()

    @property
    def value(self) -> int:
        return self.count


class AbsoluteAtomic (Singleton, Atomic):
    """
    Absolute atomic counter.

    This is a singleton class, which means there will be only one instance of this class and it will share the counter.
    """
    __init__ = Atomic.__init__


class MultitonAtomic (Multiton, Atomic):
    """
    Multiton atomic counter.

    This is a multiton class, which means that each instance of this class will have its own counter.
    """
    __init__ = Atomic.__init__


__all__ = [
    "Static",
    "Abstract",
    "abstractmethod",
    "Singleton",
    "Multiton",
    "Atomic",
    "AbsoluteAtomic",
    "MultitonAtomic"
]
