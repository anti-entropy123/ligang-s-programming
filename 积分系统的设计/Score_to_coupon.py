from Some_thing import Some_thing
import Spend_score_rule as ssr

class Score_to_coupon(Some_thing):
    id_soupon: int

    def __init__(self, id):
        super().__init__()
        self.id_soupon = id
    
    def do(self):
        return (
            0,
            ssr.score_of_coupon[self.id_soupon]
        )