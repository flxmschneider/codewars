import unittest
from nonRepeatingCharacter import first_non_repeating_letter

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_1(self):
        self.assertEqual(first_non_repeating_letter('a'), 'a')
    
    def test_2(self):
        self.assertEqual(first_non_repeating_letter('stress'), 't')
    
    def test_3(self):
        self.assertEqual(first_non_repeating_letter('moonmen'), 'e')
    
    def test_4(self):
        self.assertEqual(first_non_repeating_letter('aa'), '')
    
    def test_5(self):
        self.assertEqual(first_non_repeating_letter('~><#~><'), '#')

if __name__ == '__main__':
    unittest.main()
