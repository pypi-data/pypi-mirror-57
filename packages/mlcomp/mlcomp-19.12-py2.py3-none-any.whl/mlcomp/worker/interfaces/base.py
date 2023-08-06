from abc import ABC, abstractmethod

from mlcomp.utils.misc import to_snake


class Interface(ABC):
    _child = dict()

    def __init__(self, name: str, *args, **kwargs):
        self.name = name

    @abstractmethod
    def __call__(self, x: dict) -> dict:
        pass

    @staticmethod
    def register(cls):
        Interface._child[cls.__name__] = cls
        Interface._child[cls.__name__.lower()] = cls
        Interface._child[to_snake(cls.__name__)] = cls
        return cls

    @staticmethod
    def from_config(config: dict):
        interface = config['interface']
        if interface not in Interface._child:
            raise ModuleNotFoundError(f'Interface {interface} '
                                      f'has not been found')
        child_class = Interface._child[interface]
        return child_class(**config, **config['interface_params'])
