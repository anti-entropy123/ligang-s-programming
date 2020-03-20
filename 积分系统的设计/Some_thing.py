from abc import abstractmethod, ABCMeta

class Some_thing(metaclass=ABCMeta):
    @abstractmethod
    def do(self)->tuple:
        pass