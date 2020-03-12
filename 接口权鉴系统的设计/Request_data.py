class Request_data():
    ip_address: str
    id: str
    passwd: str
    def __init__(self, ip, id, passwd, url):
        self.ip_address = ip
        self.id = id
        self.passwd = passwd
        self.url = url