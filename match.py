class Match:
    players = []

    def addPlayer(self,player):
        self.players.append(player)

    def countPlayers(self):
        return len(self.players)

    def winPoint(self, playerIndex):
        self.players[playerIndex].incrementScore()