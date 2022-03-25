import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.x=20
        self.y=10

    def tearDown(self) :
        self.x=0
        self.y=0

    def test_add(self):
        #ACT
        result=Calculator.add(self.x,self.y)
        #ASSERT
        self.assertEqual(result,self.x+self.y)

    def test_sub(self):
        result=Calculator.sub(self.x,self.y)
        self.assertEqual(result,self.x-self.y)

    def test_mult(self):
        result=Calculator.mult(self.x,self.y)
        self.assertEqual(result,self.x*self.y)

    def test_div(self):
        result=Calculator.div(self.x,self.y)
        self.assertEqual(result,self.x/self.y)

if __name__=="__main__":
    unittest.main()
