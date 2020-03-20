from Some_thing import Some_thing
import Spend_score_rule as ssr

class Score_to_product(Some_thing):
    id_product: int

    def __init__(self, id):
        super().__init__()
        self.id_product = id
    
    def do(self):
        return (
            0,
            ssr.score_of_product[self.id_product]
        )