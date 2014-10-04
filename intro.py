import unittest
from player import Player
from match import Match
from mock import Mock
import sys

# The following is the class in which all functions will be ran by unittest
class TenisTest(unittest.TestCase):


    # Functions beginning with "test" will be ran as a unit test.
    def test_create_plater(self):
        john = Player('John')
        self.assertEqual(john.name, 'John')

    def test_inital_score(self):
        john = Player('John')
        self.assertEqual(john.getScore(), 0)

    def test_increment_score(self):
        john = Player('John')
        john.incrementScore()
        self.assertEqual(john.getScore(), 15)
        john.incrementScore()
        self.assertEqual(john.getScore(), 30)
        john.incrementScore()
        self.assertEqual(john.getScore(), 40)

    def test_new_match(self):
        RolandGarros = Match("Roland Garros")
        self.assertEqual(RolandGarros.name, 'Roland Garros')

    def test_add_player(self):
        john = Player('John')
        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer(john)

        self.assertEqual(RolandGarros.countPlayers(), 1)

        rafa = Player('Rafa')
        RolandGarros.addPlayer(rafa)

        self.assertEqual(RolandGarros.countPlayers(), 2)

    def test_win_point(self):
        john = Player('John')
        rafa = Player('Rafa')
        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer(john)
        RolandGarros.addPlayer(rafa)

        RolandGarros.winPoint(Match.PLAYER1)

        self.assertEqual(RolandGarros.getScore(Match.PLAYER1), 15)

        RolandGarros.winPoint(Match.PLAYER1)

        self.assertEqual(RolandGarros.getScore(Match.PLAYER1), 30)

        RolandGarros.winPoint(Match.PLAYER1)

        self.assertEqual(RolandGarros.getScore(Match.PLAYER1), 40)

        RolandGarros.winPoint(Match.PLAYER2)

        self.assertEqual(RolandGarros.getScore(Match.PLAYER2), 15)

        RolandGarros.winPoint(Match.PLAYER2)

        self.assertEqual(RolandGarros.getScore(Match.PLAYER2), 30)

        RolandGarros.winPoint(Match.PLAYER2)

        self.assertEqual(RolandGarros.getScore(Match.PLAYER2), 40)


    def test_win_match(self):
        '''
        john  = Player("John")
        john.getScore = Mock(return_value=30)
        rafa  = Player("Rafa")
        rafa.getScore = Mock(return_value=40)

        RolandGarros = Match()
        RolandGarros.addPlayer(john)
        RolandGarros.addPlayer(rafa)

        RolandGarros.winPoint(Match.PLAYER2)

        self.assertEqual(RolandGarros.getWinner(), Match.PLAYER2)
        '''

if __name__ == '__main__':
    unittest.main()

