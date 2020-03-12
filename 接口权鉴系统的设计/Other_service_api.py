from Api import Api
from Request_data import Request_data

class Other_service_api(Api):
    def __init__(self):
        super().__init__()
    
    def _api(self, url: str):
        pass

    def _parse_request(self, request: bytes)->Request_data:
        pass
    
    def _auth(self, Request_data)->int:
        pass

    def _refuse_response(self):
        pass

    def process_request(self, request):
        pass