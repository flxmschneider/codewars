import unittest
from script import function 

class Test(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
