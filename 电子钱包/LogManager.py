from abc import ABCMeta, abstractmethod
import ConstVar

class LogManager(metaclass = ABCMeta):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def doLog(self, userID: int, logContent: str)->int:
        pass
    @abstractmethod
    def checklog(self, userID: int)->str:
        pass