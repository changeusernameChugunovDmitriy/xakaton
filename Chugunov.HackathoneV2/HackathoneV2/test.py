import unittest
from Calculator import Caalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Caalculator()

    def test_add(self):
        """
        Тестирование сложения чисел
        """
        self.assertEqual(self.calculator.add(0.1, 0.2), 0.3)
        self.assertEqual(self.calculator.add(5, -3), 2)
        self.assertEqual(self.calculator.add(0.1, 1), 1.1)

    def test_subtract(self):
        """
        Тестирование разности чисел
        """
        self.assertEqual(self.calculator.subtract(0.1, 0.2), -0.1)
        self.assertEqual(self.calculator.subtract(-1, 3), -4)
        self.assertAlmostEqual(self.calculator.subtract(1, 0.5), 0.5)

    def test_multiply(self):
        """
        Тестирование умножения чисел
        """
        self.assertEqual(self.calculator.multiply(0.1, 0.2), 0.02)
        self.assertEqual(self.calculator.multiply(-2, 5), -10)
        self.assertAlmostEqual(self.calculator.multiply(1, 0.5), 0.5)

    def test_divide(self):
        """
        Тестирование деления чисел
        """
        self.assertEqual(self.calculator.divide(0.1, 0.2), 0.5)
        self.assertEqual(self.calculator.divide(5, -2), -2.5)
        self.assertEqual(self.calculator.divide(10, 5.5), 1.818)

        # Тестирование деления на ноль
        self.assertEqual(self.calculator.divide(5, 0), "Делить на ноль нельзя!")

    def test_readline(self):
        """
        Тестирование правильного записывания значений
        """
        line = "3 + 4"
        self.assertEqual(self.calculator.readline(line), {"a": 3.0, "b": 4.0, "f": "+", "r": "???"})

        line = "5.5 - 2.3"
        self.assertEqual(self.calculator.readline(line), {"a": 5.5, "b": 2.3, "f": "-", "r": "???"})

if __name__ == '__main__':
    unittest.main()