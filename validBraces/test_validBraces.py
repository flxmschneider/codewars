import unittest
from validBraces import validBraces

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_1(self):
        self.assertEqual(validBraces('()'), True)
    
    def test_2(self):
        self.assertEqual(validBraces('[(]'), False)
    
    def test_3(self):
        self.assertEqual(validBraces('[()]'), True)
 
    def test_4(self):
        self.assertEqual(validBraces('[(()]'), False)
    
    def test_5(self):
        self.assertEqual(validBraces(')(}{]['), False)

    def test_6(self):
        self.assertEqual(validBraces('())({}}{()][]['), False)

if __name__ == '__main__':
    unittest.main()
