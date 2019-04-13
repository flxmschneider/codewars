import unittest
from memorizedFibonacci import fibonacci 

class Test(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(fibonacci(50), 12586269025)

    def test_2(self):
        self.assertEqual(fibonacci(60), 1548008755920)

if __name__ == '__main__':
    unittest.main()
