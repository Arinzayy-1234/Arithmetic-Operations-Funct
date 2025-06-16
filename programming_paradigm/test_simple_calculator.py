

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_add(self):
        result = self.calc.add(1,2)
        self.assertEqual(result,3)
        
    def test_subtract(self):
        result = self.calc.subtract(2,1)
        self.assertEqual(result,1)
        
    def test_divide(self):
        result = self.calc.divide(4,2)
        self.assertEqual(result,2)

    def test_multiply(self):
        result = self.calc.multiply(2,2)
        self.assertEqual(result,4)
        
    def test_Zero_Division(self):
        result = self.calc.divide(4,0)
        self.assertEqual(result,None)
        
if __name__ == "__main__":
    unittest.main()
               
