from abc import ABCMeta, abstractmethod

class ThirdPartyAmountData(metaclass = ABCMeta):
    id = None
    key = None
    def __init__(self, id: str, key: str):
        super().__init__()
        self.id = id
        self.key = key
        
    @abstractmethod
    def sendCommand(self)->int:
        pass
