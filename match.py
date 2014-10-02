class Match:
    players = []

    PLAYER1 = 0
    PLAYER2 = 1

    def addPlayer(self,player):
        self.players.append(player)

    def countPlayers(self):
        return len(self.players)

    def winPoint(self, playerIndex):
        self.players[playerIndex].incrementScore()

    def getPlayer(self,playerIndex):
        return self.players[playerIndex]