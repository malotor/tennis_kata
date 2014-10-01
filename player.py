class Player:
    score = 0

    def __init__(self, name):
        self.name = name

    def winPoint(self):
        self.score = 15