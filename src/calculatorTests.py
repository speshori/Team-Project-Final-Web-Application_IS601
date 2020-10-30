import unittest
from calculator import calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calc, calculator)

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 2), 4)

if __name__ == '__main__':
    unittest.main()
