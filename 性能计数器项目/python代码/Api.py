from abc import ABCMeta, abstractmethod

class Api(metaclass=ABCMeta):
    @abstractmethod
    def service(self):
        pass
