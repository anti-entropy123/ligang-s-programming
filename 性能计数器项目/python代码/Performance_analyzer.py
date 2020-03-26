from abc import ABCMeta, abstractmethod

class Performance_analyzer(metaclass=ABCMeta):
    @abstractmethod
    def before_service(self):
        pass
    @abstractmethod
    def after_service(self):
        pass