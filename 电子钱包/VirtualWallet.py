from ThirdPartyAmountData import ThirdPartyAmountData as TPAD
from SystemBankManager import SystemBankManager as SBM
from LogManager import LogManager
import ConstVar

class VirtualWallet():
    userMoney = {}  # 存放所有用户的金额数据, 实际中应使用数据库
    systemBankAmount: TPAD = None
    bankManager: SBM = None
    logManager: LogManager = None
    
    def __init__(self, sba: TPAD):
        self.bankManager = SBM(sba)
        self.logManager = LogManager()
    
    def pay(self, payerID: int, receiverID: int, amount: float)->int:
        try:
            self.userMoney[payerID] -= amount
            self.userMoney[receiverID] += amount
            self.logManager.doLog()
            return ConstVar.successCode
        except Exception as e:
            return ConstVar.failCode
    
    def recharge(self, userID: int, userAmount: TPAD, amount: float)->int:
        try:
            self.bankManager.transfer(sender=userAmount, receiver=self.systemBankAmount, amount=amount)
            self.userMoney[userID] += amount
            self.logManager.doLog()
            return ConstVar.successCode
        except Exception as e:
            return ConstVar.failCode

    def withDraw(self, userID: int, userAmount: TPAD, amount: float)->int:
        try:
            self.bankManager.transfer(sender=self.systemBankAmount, receiver=userAmount, amount=amount)
            self.userMoney[userID] -= amount
            self.logManager.doLog()
            return ConstVar.successCode
        except Exception as e:
            return ConstVar.failCode
        
    def checkBalance(self, userID: int)->float:
        return self.userMoney[userID]
    
    def checkLog(self, userID: int)->str:
        try:
            return self.logManager.checklog(userID=userID)
        except Exception as e:
            return ConstVar.failCode
            