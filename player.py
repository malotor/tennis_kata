class Player:

    scores = [ 0 , 15 , 30 , 40 ]
    currentScore = 0

    def __init__(self, name):
        self.name = name

    def getScore(self):
        return self.scores[self.currentScore]

    def winPoint(self):
        self.currentScore = self.currentScore + 1
