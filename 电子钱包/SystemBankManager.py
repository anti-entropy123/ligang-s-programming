import ConstVar
from ThirdPartyAmountData import ThirdPartyAmountData as TPAD

class SystemBankManager():
    SystemBankAmount = None
    def __init__(self, sba):
        self.SystemBankAmount = sba
    def transfer(self, sender: TPAD, receiver: TPAD, amount: float) -> int: 
        try:
            sender.sendCommand()
            receiver.sendCommand()
            return ConstVar.successCode
        except Exception as e:
            return ConstVar.failCode
