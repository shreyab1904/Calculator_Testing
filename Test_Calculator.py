import main
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        x=10
        y=20
        result=Calculator.add(x,y)
        self.assertEqual(result,x+y)
    def test_sub(self):
        x=20
        y=10
        result=Calculator.sub(x,y)
        self.assertEqual(result,x-y)
    def test_mult(self):
        x=10
        y=20
        result=Calculator.mult(x,y)
        self.assertEqual(result,x*y)
    def test_div(self):
        x=10
        y=5
        result=Calculator.div(x,y)
        self.assertEqual(result,x/y)

if __name__=="__main__":
    unittest.main()
