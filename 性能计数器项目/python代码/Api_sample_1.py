from proxy import proxy
from Api import Api
from time import sleep
from random import random

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
