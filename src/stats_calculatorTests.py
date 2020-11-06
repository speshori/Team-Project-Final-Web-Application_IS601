import unittest
from stats_calculator import stats_calculator
import statistics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = stats_calculator()
        self.lst = [0, 1, 2, 3, 3]

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calc, stats_calculator)

    # RANDOM GENERATOR FUNCTIONS' TESTS
    def test_random_num_int_generator(self):
        self.assertIs(type(self.calc.random_num_int_generator()), int)

    def test_random_num_float_generator(self):
        self.assertIs(type(self.calc.random_num_float_generator()), float)

    def test_random_num_seed_int_generator(self):
        self.assertIs(type(self.calc.random_num_seed_int_generator()), int)

    def test_random_num_seed_float_generator(self):
        self.assertIs(type(self.calc.random_num_seed_float_generator()), float)

    def test_list_seed_int_generator(self):
        self.assertIs(type(self.calc.list_seed_int_generator()), list)

    def test_list_seed_float_generator(self):
        self.assertIs(type(self.calc.list_seed_float_generator()), list)

    def test_random_item_generator(self):
        self.assertIs(type(self.calc.random_item_generator(self.lst)), int)

    def test_random_seed_item_generator(self):
        self.assertIs(type(self.calc.random_seed_item_generator(self.lst)), int)

    def test_select_range_generator(self):
        self.assertIs(type(self.calc.select_range_generator(self.lst)), list)

    def test_select_seed_range_generator(self):
        self.assertIs(type(self.calc.select_seed_range_generator(self.lst)), list)

    # DESCRIPTIVE STATISTICS FUNCTIONS' TESTS
    def test_mean(self):
        self.assertEqual(self.calc.mean(self.lst), statistics.mean(self.lst))

    def test_median(self):
        self.assertEqual(self.calc.median(self.lst), statistics.median(self.lst))

    def test_mode(self):
        self.assertEqual(self.calc.mode(self.lst), statistics.mode(self.lst))

    def test_variance(self):
        self.assertEqual(self.calc.variance(self.lst), statistics.variance(self.lst))

    def test_standard_deviation(self):
        self.assertEqual(self.calc.standard_deviation(self.lst), float("{:.3f}".format(float(statistics.stdev(self.lst))))  )

    def test_z_score(self):
        self.assertIs(type(self.calc.z_score(self.lst)), list)

if __name__ == '__main__':
    unittest.main()
