import unittest
import player
import match

# The following is the class in which all functions will be ran by unittest
class TenisTest(unittest.TestCase):
    def setUp(self):
        self.john = player.Player('John')
        self.rafa = player.Player('Rafa')
        self.RolandGarros = match.Match()

        '''Verify environment is setup properly'''  # Printed if test fails
        pass

    # The function "tearDown" will always be ran in order to cleanup the
    # test environment after all the tests have run.
    def tearDown(self):
        '''Verify environment is tore down properly'''  # Printed if test fails
        pass

    # Functions beginning with "test" will be ran as a unit test.
    def test_create_plater(self):
        self.assertEqual(self.john.name, 'John')

    def test_inital_score(self):
        self.assertEqual(self.john.getScore(), 0)

    def test_increment_score(self):
        self.john.incrementScore()
        self.assertEqual(self.john.getScore(), 15)
        self.john.incrementScore()
        self.assertEqual(self.john.getScore(), 30)
        self.john.incrementScore()
        self.assertEqual(self.john.getScore(), 40)

    def test_new_match(self):
        RolandGarros = match.Match()

    def test_add_player(self):
        self.RolandGarros.addPlayer(self.john)

        self.assertEqual(self.RolandGarros.countPlayers(), 1)

        self.RolandGarros.addPlayer(self.rafa)

        self.assertEqual(self.RolandGarros.countPlayers(), 2)

    def test_win_point(self):

        self.RolandGarros.winPoint(0)

        self.assertEqual(self.john.getScore(), 15)



if __name__ == '__main__':
    unittest.main()

