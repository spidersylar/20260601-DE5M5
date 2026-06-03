import unittest 
from tests_demo.calc import Calculator 

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.data = [(8,2,10,6,16,4),
                (10,5,15,5,50,2),
                (10,0,10,10,0,10)]
    def test_sum(self):
        for a,b, expected, _, _, _ in self.data:
            calc = Calculator(a, b)
            self.assertEqual(calc.get_sum(), expected, f"Failed sum for {a} and {b}")

    def test_difference(self):
        for a,b, _, expected, _, _ in self.data:
            calc = Calculator(a, b)
            self.assertEqual(calc.difference(), expected, f"Failed difference for {a} and {b}")

    def test_product(self):
        for a,b, _, _, expected, _ in self.data:
            calc = Calculator(a, b)
            self.assertEqual(calc.product(), expected, f"Failed product for {a} and {b}")

    def test_quotient(self):
        for a,b, _, _, _, expected in self.data:
            if b == 0: 
                pass
            else:
                calc = Calculator(a, b)
                self.assertEqual(calc.quotient(), expected, f"Failed quotient for {a} and {b}")

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()