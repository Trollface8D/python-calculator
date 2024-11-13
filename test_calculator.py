import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 2), 1)

        self.assertEqual(self.calc.subtract(10,4),6)
        self.assertEqual(self.calc.subtract(-3,2),-5)

        self.assertEqual(self.calc.multiply(3,2),6)
        self.assertEqual(self.calc.multiply(-5,-10),50)

        self.assertEqual(self.calc.divide(6,2),3)
        self.assertEqual(self.calc.divide(-10,2),-5)

        self.assertEqual(self.calc.modulo(5,2),1)
        self.assertEqual(self.calc.modulo(100,10),0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()