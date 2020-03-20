from Some_thing import Some_thing
import Get_score_rule as gsr

class Comment(Some_thing):
    def do(self):
        return (
            1, 
            gsr.score_of_comment, 
            gsr.live_comment
        )