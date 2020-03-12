from abc import ABCMeta, abstractmethod
from Authentication import Authentication
from Request_data import Request_data

class Api(metaclass=ABCMeta):
    judger: Authentication = None
    
    def Api(self):
        self.judger = Authentication()
    
    @abstractmethod
    def _api(self, url: str)->bytes:
        pass
    
    @abstractmethod
    def _parse_request(self, request: bytes)->Request_data:
        pass

    @abstractmethod
    def _auth(self, data:Request_data)->int:
        pass

    @abstractmethod
    def _refuse_response(self)->bytes:
        pass
    
    @abstractmethod
    def process_request(self, request: bytes)->bytes:
        pass
