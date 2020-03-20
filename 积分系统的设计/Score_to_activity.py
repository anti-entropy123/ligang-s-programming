from Some_thing import Some_thing
import Spend_score_rule as ssr

class Score_to_activity(Some_thing):
    id_activity: int
    
    def __init__(self, id):
        super().__init__()
        self.id_activity = id
    
    def do(self):
        return (
            0, 
            ssr.score_of_activity[self.id_activity]
        )
    