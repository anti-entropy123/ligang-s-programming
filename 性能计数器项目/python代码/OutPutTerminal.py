from abc import ABCMeta, abstractmethod

class OutPut_terminal(metaclass=ABCMeta):
    @abstractmethod
    def out_put(self, data: str):
        pass