from Some_thing import Some_thing
import Get_score_rule as gsr

class Sign_in_daily(Some_thing):
    def do(self):
        return (
            1, 
            gsr.score_of_sign_in, 
            gsr.live_of_sign_in
        )
