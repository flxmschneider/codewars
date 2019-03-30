import unittest
from highest_scoring import high 

class Test(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(high('man i need a taxi up to ubud'), 'taxi')
    
    def test_2(self):
        self.assertEqual(high('what time are we climbing up the volcano'), 'volcano')

if __name__ == '__main__':
    unittest.main()
