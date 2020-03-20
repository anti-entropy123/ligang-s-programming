from Some_thing import Some_thing
import Get_score_rule as gsr

class Place_an_order(Some_thing):
    amount: float
    def __init__(self, amount):
        super().__init__()
        self.amount = amount
    def do(self):
        return (
            1, 
            self.amount*gsr.ratio_amount_to_score, 
            gsr.live_amount
        )
