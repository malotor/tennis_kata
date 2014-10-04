class Match:
    players = []

    PLAYER1 = 0
    PLAYER2 = 1

    scores = [ 0 , 15 , 30 , 40, 'adv', 'win']

    winner = None

    def __init__(self, name):
        self.name = name

    def addPlayer1(self,player):
        self.players.insert( self.PLAYER1, player)

    def addPlayer2(self,player):
        self.players.insert( self.PLAYER2, player)

    def countPlayers(self):
        return len(self.players)

    def winPoint(self, player):
        if (player == self.PLAYER1):
            oponent = self.PLAYER2
        else:
            oponent = self.PLAYER1

        playerScore = self.getScore(player)
        openentScore = self.getScore(oponent)

        if (playerScore == 40 and  openentScore < 40):
            self.winner = player
            self.players[player].incrementScore()
            self.players[player].incrementScore()
        elif (playerScore == 'adv' and openentScore == 40):
            self.winner = player
            self.players[player].incrementScore()
        #Get adv
        elif (playerScore == 40 and  openentScore == 40):
            self.players[player].incrementScore()
        #Lose av
        elif (playerScore == 40  and  openentScore == 'adv'):
            self.players[oponent].decrementScore()
        else:
            self.players[player].incrementScore()

    def getPlayer(self,player):
        return self.players[player]

    def getScore(self,player):
        playerScore = self.players[player].getScore()
        return self.scores[playerScore]

    def getWinner(self):
        return self.winner