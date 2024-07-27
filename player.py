class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0


    # increment score of player
    def increment_score(self):
        self.score += 1
