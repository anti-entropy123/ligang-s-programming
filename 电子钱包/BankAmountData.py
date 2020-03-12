from ThirdPartyAmountData import ThirdPartyAmountData as TPAD
import ConstVar

class BankAmountData(TPAD):
    def __init__(self, id, key):
        super().__init__(id, key)
    def sendCommand(self)->int:
        try:
            # 与银行发送转账指令, 此处略
            return ConstVar.successCode
        except Exception as e:
            return ConstVar.failCode