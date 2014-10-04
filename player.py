class Player:

    currentScore = 0

    def __init__(self, name):
        self.name = name

    def getScore(self):
        return self.currentScore

    def incrementScore(self):
        self.currentScore = self.currentScore + 1

    def decrementScore(self):
        self.currentScore = self.currentScore + 1