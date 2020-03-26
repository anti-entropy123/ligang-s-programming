from Performance_analyzer import Performance_analyzer
from time import time
from OutPutTerminal import OutPut_terminal
import json 
class Analyzer_sample_1(Performance_analyzer):
    _count = 0
    _response_time: list = []
    _start_time: double = 0
    _cache = {}

    def __init__(self):
        self._start_time = time()

    def before_service(self, key):
        self.count += 1
        self._cache[key] = time()

    def after_service(self, key):
        self._response_time.append(time()-self._cache[key])
        try:
            self._cache.popitem(key)
        except KeyError as e:
            print('key error Exception')
    
    def get_Max_Response_time(self)->float:
        return max(self._response_time)

    def get_Min_Response_time(self)->float:
        return min(self._response_time)
    
    def get_tps(self)->float:
        return len(self._response_time)/(time()-self._start_time)
    
    def get_count(self)->int:
        return self._count
    
    def result2json(self)->str:
        result = {
            'max_response_time': self.get_Max_Response_time(),
            'min_response_time': self.get_Min_Response_time(),
            'tps': self.get_tps(),
            'count': self.get_count()
        }
        return json.dumps(result)

    def result2html(self)->str:
        return 'html data ...'
    
    def out_put(self, terminal: OutPut_terminal, data: str):
        terminal.out_put(data)

analyzer = Analyzer_sample_1()