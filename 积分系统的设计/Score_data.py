from time import time, localtime, strftime

class Score_data():
    _score: int
    _create_data: time()
    _lived_days: int
    def __init__(self, s: int, ld: int):
        self._score = s
        self._create_data = time()
        self._lived_days = ld

    @property
    def score(self)->int:
        return self._score
    
    @score.setter
    def score(self, s: int):
        self._score = s

    def is_out_of_data(self)->bool:
        return (time()-self._create_data) > self._lived_days*24*3600
    
    def detail_info(self)->str:
        return "积分: {score}\n被创建于: {time}\n有效期: {day} 天".format(
            score = self._score,
            time = strftime("%Y-%m-%d", localtime(self._create_data)),
            day = self._lived_days
        )

    def get_remain_time(self)->int:
        return (self._lived_days*24*3600-(time()-self._create_data))//(3600*24)
