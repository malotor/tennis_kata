class Player:
    score = 0

    def __init__(self, name):
        self.name = name
    def getScore(self):
        return self.score;
    def winPoint(self):
        if self.score == 0:
            self.score = 15
        elif self.score == 15:
            self.score = 30
        elif self.score == 30:
            self.score = 40
