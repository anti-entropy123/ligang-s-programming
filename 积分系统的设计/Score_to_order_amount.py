from Some_thing import Some_thing
import Spend_score_rule as ssr

class Score_to_order_amount(Some_thing):
    amount: float

    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def do(self):
        return (
            0, 
            self.amount*ssr.radio_score_to_amount
        )