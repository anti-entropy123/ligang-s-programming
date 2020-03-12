from Request_data import Request_data
import config

class Authentication():
    def __init__(self):
        pass

    def _ip_judge(self, data: Request_data)->bool:
        return data.ip_judge in config.authenticate_id_address

    def _passwd_judge(self, data: Request_data)->bool:
        return data.passwd == config.id_password.get(data.id, None)

    def judge(self, data: Request_data)->int:
        if not self.ip_judge(data):
            return config.non_auth_ip
        elif not self.passwd_judge(data):
            return config.wrong_id_or_passwd
        else:
            return config.auth_success
        
        