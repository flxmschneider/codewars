import unittest
from string_incrementer import increment_string 

class Test(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(increment_string('foo'),'foo1')
    
    def test_2(self):
        self.assertEqual(increment_string('foo01'),'foo02')

if __name__ == '__main__':
    unittest.main()
