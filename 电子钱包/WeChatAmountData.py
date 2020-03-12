from ThirdPartyAmountData import ThirdPartyAmountData as TPAD
import ConstVar

class WeChatAmountData(TPAD):
    def __init__(self, id, key):
        super().__init__(id, key)
    def sendCommand(self)->int:
        try: 
            # 向微信发送转账指令
            return ConstVar.successCode
        except Exception as e:
            return ConstVar.failCode