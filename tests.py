import unittest
from player import Player
from match import Match
from mock import Mock

# The following is the class in which all functions will be ran by unittest
class TenisTest(unittest.TestCase):


    # Functions beginning with "test" will be ran as a unit test.
    def test_create_plater(self):
        john = Player('John')
        self.assertEqual(john.name, 'John')

    def test_inital_score(self):
        john = Player('John')
        self.assertEqual(john.getScore(), 0)

    '''
    def test_increment_score(self):
        john = Player('John')
        john.incrementScore()
        self.assertEqual(john.getScore(), 15)
        john.incrementScore()
        self.assertEqual(john.getScore(), 30)
        john.incrementScore()
        self.assertEqual(john.getScore(), 40)
    '''

    def test_new_match(self):
        RolandGarros = Match("Roland Garros")
        self.assertEqual(RolandGarros.name, 'Roland Garros')

    def test_add_player(self):
        john = Player('John')
        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)

        self.assertEqual(RolandGarros.countPlayers(), 1)

        rafa = Player('Rafa')
        RolandGarros.addPlayer2(rafa)

        self.assertEqual(RolandGarros.countPlayers(), 2)

    def test_win_point(self):
        john = Player('John')
        rafa = Player('Rafa')
        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

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

#scores = [ 0 , 15 , 30 , 40, 'adv', 'win']
    def test_win_match_with_diferente_of_two(self):

        john  = Player("John")
        john.getScore = Mock(return_value=2)
        rafa  = Player("Rafa")
        rafa.getScore = Mock(return_value=3)

        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER2)

        self.assertEqual(RolandGarros.getWinner(), Match.PLAYER2)


    def test_win_match_with_adv(self):

        john  = Player("John")
        john.getScore = Mock(return_value=3)
        rafa  = Player("Rafa")
        rafa.getScore = Mock(return_value=4)

        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER2)

        self.assertEqual(RolandGarros.getWinner(), Match.PLAYER2)


    def test_no_winner(self):

        john  = Player("John")
        john.getScore = Mock(return_value=3)
        rafa  = Player("Rafa")
        rafa.getScore = Mock(return_value=3)

        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER2)
        self.assertIsNone(RolandGarros.getWinner())


    def test_loose_advance(self):

        john  = Player("John")
        john.getScore = Mock(return_value=4)
        rafa  = Player("Rafa")
        rafa.getScore = Mock(return_value=5)
        # 40 / Adv
        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER1)
        self.assertIsNone(RolandGarros.getWinner())


if __name__ == '__main__':
    unittest.main()

