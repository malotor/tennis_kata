class Match:
    players = []

    def addPlayer(self,player):
        self.players.append(player)

    def countPlayers(self):
        return len(self.players)