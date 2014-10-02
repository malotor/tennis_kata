class Match:
    players = []

    PLAYER1 = 0
    PLAYER2 = 1

    def addPlayer(self,player):
        self.players.append(player)

    def countPlayers(self):
        return len(self.players)

    def winPoint(self, player):
        self.players[player].incrementScore()

    def getPlayer(self,player):
        return self.players[player]

    def getScore(self,player):
        return self.players[player].getScore()
