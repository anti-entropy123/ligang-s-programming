from Score_data import Score_data
from functools import cmp_to_key
from Some_thing import Some_thing

class Score_data():
    _all_data: List[Score_data] = []
    
    def __init__(self):
        pass
    
    def total_score(self)->int:
        self._check_all_score_record()
        return sum([i.score for i in self._all_data])
    
    def score_log(self)->str:
        return "\n\n".join([i.detail_info() for i in self._all_data])
    
    def do_things(self, s: Some_thing)->int:
        self._check_all_score_record()
        option = s.do()
        if option[0]:
            # 存入积分
            # [type ,score, live_days]
            self._all_data.append(Score_data(option[1], option[2]))
            self._sort_list_as_remain()
        else:
            # 使用积分
            # [type, score]
            if self.total_score() > option[1]:
                # 剩余积分足够
                while option[1] >= self._all_data[-1].score:
                    option[1] -= self._all_data[-1].score
                    self._all_data.pop()
                self._all_data[-1].score -= option[1]
            else:
                # 剩余积分不足
                raise Exception("剩余积分不足")
            

    def _check_all_score_record(self):
        self._all_data = list(filter(lambda x: x.is_out_of_date(), self._all_data))
    
    def _sort_list_as_remain(self):
        key = cmp_to_key(lambda x,y: -1 if x.get_remain_time()>y.get_remain_time() else 1)
        self._all_data = sorted(self._all_data, key=key)
    