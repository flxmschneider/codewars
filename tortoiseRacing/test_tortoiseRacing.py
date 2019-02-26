import unittest
from tortoiseRacing import race 

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(race(720, 850, 70), [0, 32, 18])

    def test_2(self):
        self.assertEqual(race(80, 91, 37), [3, 21, 49])

if __name__ == '__main__':
    unittest.main()
