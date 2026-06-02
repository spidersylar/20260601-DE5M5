import unittest 
from calc import Calculator 

class TestOperations(unittest.TestCase):
    def setUp(self):
        data = [(8,2),(10,0)]
        self.calc = Calculator(8,2)
    def test_sum(self):
        self.assertEqual(self.calc.get_sum(), 10, "The answer was not 10")

    def test_difference(self):
        self.assertEqual(self.calc.difference(), 6, "The answer was not 6")

    def test_product(self):
        self.assertEqual(self.calc.product(), 16, "The answer was not 16")

    def test_quotient(self):
        self.assertEqual(self.calc.quotient(), 4, "The answer was not 4")

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()