
import unittest
import player

# The following is the class in which all functions will be ran by unittest
class TenisTest(unittest.TestCase):
   def setUp(self):
      '''Verify environment is setup properly''' # Printed if test fails
      pass

   # The function "tearDown" will always be ran in order to cleanup the
   # test environment after all the tests have run.
   def tearDown(self):
      '''Verify environment is tore down properly''' # Printed if test fails
      pass

   # Functions beginning with "test" will be ran as a unit test.
   def test_create_plater(self):
       john = player.Player('John')
       self.assertEqual(john.name, 'John')



if __name__=='__main__':
   unittest.main()

