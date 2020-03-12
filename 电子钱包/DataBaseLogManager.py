from LogManager import LogManager
import ConstVar

class DataBaseLogManager(LogManager):
    def __init__(self):
        super().__init__()

    def doLog(self, userID: int, logContent: str)->int:
        try:
            # do something
            return ConstVar.successCode
        except Exception as e:
            return ConstVar.failCode
    
    def checklog(self, userID: int)->str:
        try:
            # do something
            resultOfCheckLog = None
            return resultOfCheckLog
        except Exception as e:
            return ConstVar.failCode
    