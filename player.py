class Player:

    scores = [ 0 , 15 , 30 , 40, 'win']
    currentScore = 0

    def __init__(self, name):
        self.name = name

    def getScore(self):
        return self.scores[self.currentScore]

    def incrementScore(self):
        self.currentScore = self.currentScore + 1
