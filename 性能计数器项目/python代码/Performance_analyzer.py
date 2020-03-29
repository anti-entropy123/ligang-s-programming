from abc import ABCMeta, abstractmethod
from time import time
from OutPutTerminal import OutPut_terminal
import json

class Performance_analyzer(metaclass=ABCMeta):
    @abstractmethod
    def before_service(self):
        pass
    @abstractmethod
    def after_service(self):
        pass


class Analyzer_sample_1(Performance_analyzer):    
    def __init__(self):
        self._count = 0
        self._start_time = time()
        self._response_time = []
        self._cache = {}

    def before_service(self, key):
        self._count += 1
        self._cache[key] = time()

    def after_service(self, key):
        self._response_time.append(time()-self._cache[key])
        try:
            self._cache.pop(key)
        except KeyError as e:
            print('key error Exception')
    
    def get_max_response_time(self)->float:
        return max(self._response_time)

    def get_min_response_time(self)->float:
        return min(self._response_time)
    
    def get_avg_response_time(self)->float:
        return sum(self._response_time)/self._count

    def get_tps(self)->float:
        return self._count/(time()-self._start_time)
    
    def get_count(self)->int:
        return self._count
    
    def result2json(self)->str:
        result = {
            'max_response_time': self.get_max_response_time(),
            'min_response_time': self.get_min_response_time(),
            'avg_response_time': self.get_avg_response_time(),
            'tps': self.get_tps(),
            'count': self.get_count()
        }
        return json.dumps(result)

    def result2html(self)->str:
        return 'html data ...'
    
    def out_put(self, terminal, data: str):
        terminal.out_put(data)

class Analyzer_sample_2(Performance_analyzer):
    pass
