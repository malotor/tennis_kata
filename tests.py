import unittest
from player import Player
from match import Match
#from mock import Mock

# The following is the class in which all functions will be ran by unittest
class TenisTest(unittest.TestCase):


    # Functions beginning with "test" will be ran as a unit test.
    def test_create_plater(self):
        john = Player('John')
        self.assertEqual(john.name, 'John')

    def test_inital_score(self):
        john = Player('John')
        self.assertEqual(john.getScore(), 0)

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
    '''
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

    '''
    def test_win_player1_match_with_diferente_of_two(self):

        john  = Player("John")

        rafa  = Player("Rafa")


        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER1) # 15 / 0
        RolandGarros.winPoint(Match.PLAYER1) # 30 / 0
        RolandGarros.winPoint(Match.PLAYER1) # 40 / 0
        RolandGarros.winPoint(Match.PLAYER1) # Win / 0

        self.assertEqual(RolandGarros.getWinner(), Match.PLAYER1)

    def test_win_player2_match_with_diferente_of_two(self):

        john  = Player("John")

        rafa  = Player("Rafa")


        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER2) # 15 / 0
        RolandGarros.winPoint(Match.PLAYER2) # 30 / 0
        RolandGarros.winPoint(Match.PLAYER2) # 40 / 0
        RolandGarros.winPoint(Match.PLAYER2) # Win / 0

        self.assertEqual(RolandGarros.getWinner(), Match.PLAYER2)



    def test_player1_get_advance(self):

        john  = Player("John")

        rafa  = Player("Rafa")


        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER1) # 15 / 0
        RolandGarros.winPoint(Match.PLAYER1) # 30 / 0
        RolandGarros.winPoint(Match.PLAYER1) # 40 / 0

        RolandGarros.winPoint(Match.PLAYER2) # 15 / 0
        RolandGarros.winPoint(Match.PLAYER2) # 30 / 0
        RolandGarros.winPoint(Match.PLAYER2) # 40 / 0

        RolandGarros.winPoint(Match.PLAYER1) # adv / 40

        self.assertEqual(RolandGarros.getScore(Match.PLAYER1), 'adv')
        self.assertIsNone(RolandGarros.getWinner())


    def test_player1_loose_advance(self):

        john  = Player("John")

        rafa  = Player("Rafa")


        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER1) # 15 / 0
        RolandGarros.winPoint(Match.PLAYER1) # 30 / 0
        RolandGarros.winPoint(Match.PLAYER1) # 40 / 0

        RolandGarros.winPoint(Match.PLAYER2) # 15 / 0
        RolandGarros.winPoint(Match.PLAYER2) # 30 / 0
        RolandGarros.winPoint(Match.PLAYER2) # 40 / 0

        RolandGarros.winPoint(Match.PLAYER1) # adv / 40

        RolandGarros.winPoint(Match.PLAYER2) # 40 / 40

        self.assertEqual(RolandGarros.getScore(Match.PLAYER2), 40)
        self.assertEqual(RolandGarros.getScore(Match.PLAYER1), 40)

        self.assertIsNone(RolandGarros.getWinner())

    def test_player1_get_win_with_advance(self):

        john  = Player("John")

        rafa  = Player("Rafa")

        RolandGarros = Match("Roland Garros")
        RolandGarros.addPlayer1(john)
        RolandGarros.addPlayer2(rafa)

        RolandGarros.winPoint(Match.PLAYER1) # 15 / 0
        RolandGarros.winPoint(Match.PLAYER1) # 30 / 0
        RolandGarros.winPoint(Match.PLAYER1) # 40 / 0

        RolandGarros.winPoint(Match.PLAYER2) # 15 / 0
        RolandGarros.winPoint(Match.PLAYER2) # 30 / 0
        RolandGarros.winPoint(Match.PLAYER2) # 40 / 0

        RolandGarros.winPoint(Match.PLAYER1) # adv / 40

        RolandGarros.winPoint(Match.PLAYER1) # Win / 40

        self.assertEqual(RolandGarros.getScore(Match.PLAYER1), 'win')
        self.assertEqual(RolandGarros.getWinner(), Match.PLAYER1)


if __name__ == '__main__':
    unittest.main()

