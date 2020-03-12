from Api import Api
from Request_data import Request_data
import config

class HTTP_service_api(Api):
    def __init__(self):
        super().__init__()

    def _api(self, url: str)->bytes:
        """服务的真正提供者"""
        return "service content".encode()
    
    def _parse_request(self, request: bytes)->Request_data:
        """直接处理http流, 提取关键数据"""
        # do something, get important data from request
        data = {
            'ip' : "something",
            'id' : "something",
            'passwd' : "something",
            'url' : "something"
        }
        return Request_data(**data)
    
    def _auth(self, data:Request_data)->int:
        """对请求者认证身份"""
        return self.judger.judge(data)

    def _refuse_response(self, code: int)->bytes:
        """当拒绝提供服务时, 做出的响应"""
        return config.refuse_response.get(code, "").encode()
        
    def process_request(self, request: bytes)->bytes:
        """对请求的处理流程"""
        data = self._parse_request(request)
        code = self._auth(data)
        if code == config.auth_success:
            return self.api(data.url)
        else:
            return self._refuse_response(code)
