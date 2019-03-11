import unittest
from bouncingBalls import bouncingBall 

class Test(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(bouncingBall(3,0.66,1.5),3)
    
    def test_2(self):
        self.assertEqual(bouncingBall(30,0.66,1.5),15)


if __name__ == '__main__':
    unittest.main()
