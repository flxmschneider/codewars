import unittest
from duplicateEncode import duplicate_encode 

class Test(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(duplicate_encode("din"),"(((")
    def test_2(self):
        self.assertEqual(duplicate_encode("recede"),"()()()")

if __name__ == '__main__':
    unittest.main()
