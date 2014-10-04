from player import Player
from match import Match
import random

john = Player('John')
rafa = Player('Rafa')
RolandGarros = Match("Roland Garros")
RolandGarros.addPlayer1(john)
RolandGarros.addPlayer2(rafa)

while RolandGarros.getWinner() is None:
    pointWinner = random.choice([Match.PLAYER1,Match.PLAYER2]);
    player = RolandGarros.getPlayer(pointWinner)
    RolandGarros.winPoint(pointWinner)
    print 'Player ' + player.name +  ' win point - Current score: ' + str(RolandGarros.getScore(Match.PLAYER1)) + ' / ' + str(RolandGarros.getScore(Match.PLAYER2))

winner = RolandGarros.getPlayer(pointWinner)
print 'The winner is ' + winner.name
