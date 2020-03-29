from abc import ABCMeta, abstractmethod
from proxy import proxy
from time import sleep
from random import random

class Api(metaclass=ABCMeta):
    @abstractmethod
    def service(self):
        pass

class Api_sample_1(Api):
    def __init__(self, analyzer):
        self.func = self.service

        @proxy(analyzer)
        def t():
            return self.func()
        
        self.service = t

    def service(self):
        sleep(random())
        return "hello_world"

class Api_sample_2(Api):
    pass