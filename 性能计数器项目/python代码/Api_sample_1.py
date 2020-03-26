from proxy import proxy
from Api import Api
from Analyzer_sample_1 import analyzer

class Api_sample_1(Api):
    def __init__(self):
        self.analyzer = analyzer
        # print(self.analyzer)
        
    @proxy(analyzer)
    def service(self):
        return "hello_world"

api = Api_sample_1()