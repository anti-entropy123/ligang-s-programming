from abc import ABCMeta, abstractmethod

class OutPut_terminal(metaclass=ABCMeta):
    @abstractmethod
    def out_put(self, data: str):
        pass

class HTTP(OutPut_terminal):
    def out_put(self, data: str):
        """show data by HTTP"""

class Console(OutPut_terminal):
    def out_put(self, data):
        """show data by Console"""
    
class Email(OutPut_terminal):
    def out_put(self, data):
        """show data by Email"""

class File_log(OutPut_terminal):
    def out_put(self, data):
        """show data by File"""

class Costom(OutPut_terminal):
    def out_put(self, data):
        """show data by Costom"""
