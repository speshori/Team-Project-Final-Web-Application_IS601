import unittest
import csv
from calculator import calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calc, calculator)

    def test_addition(self):
        with open('Unit Test Addition.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertEqual(self.calc.add(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))

    def test_subtraction(self):
        with open('Unit Test Subtraction.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertEqual(self.calc.subtract(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))


    def test_multiplication(self):
        with open('Unit Test Multiplication.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertEqual(self.calc.multiply(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))

    def test_division(self):
        with open('Unit Test Division.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertEqual(self.calc.divide(int(row['Value 2']), int(row['Value 1'])), float("{:.3f}".format(float(row['Result']))))

    def test_square(self):
        with open('Unit Test Square.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertEqual(self.calc.square(int(row['Value 1'])), int(row['Result']))


    def test_squareRoot(self):
        with open('Unit Test Square Root.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertEqual(self.calc.squareroot(int(row['Value 1'])), float("{:.3f}".format(float(row['Result']))))


if __name__ == '__main__':
    unittest.main()
