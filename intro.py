import unittest
import player
import match

# The following is the class in which all functions will be ran by unittest
class TenisTest(unittest.TestCase):
    def setUp(self):
        self.john = player.Player('John')
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
        self.assertEqual(self.john.score, 0)

    def test_win_point(self):
        self.john.winPoint()
        self.assertEqual(self.john.score, 15)
        self.john.winPoint()
        self.assertEqual(self.john.score, 30)
        self.john.winPoint()
        self.assertEqual(self.john.score, 40)

    def test_new_match(self):
        RolandGarros = match.Match()

if __name__ == '__main__':
    unittest.main()

