import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5, "2 + 3 should equal 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "-1 + 1 should equal 0")
        self.assertEqual(self.calc.add(0, 0), 0, "0 + 0 should equal 0")
        self.assertEqual(self.calc.add(-5, -3), -8, "-5 + -3 should equal -8")
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0, "1.5 + 2.5 should equal 4.0")

    def test_subtract(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2, "5 - 3 should equal 2")
        self.assertEqual(self.calc.subtract(3, 5), -2, "3 - 5 should equal -2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "0 - 0 should equal 0")
        self.assertEqual(self.calc.subtract(-2, -3), 1, "-2 - (-3) should equal 1")
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0, "5.5 - 2.5 should equal 3.0")

    def test_multiply(self):
        """Test the multiply method with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6, "2 * 3 should equal 6")
        self.assertEqual(self.calc.multiply(-2, 3), -6, "-2 * 3 should equal -6")
        self.assertEqual(self.calc.multiply(0, 5), 0, "0 * 5 should equal 0")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "-2 * -3 should equal 6")
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0, "1.5 * 2 should equal 3.0")

    def test_divide(self):
        """Test the divide method with various inputs, including division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5.0, "10 / 2 should equal 5.0")
        self.assertEqual(self.calc.divide(-10, 2), -5.0, "-10 / 2 should equal -5.0")
        self.assertEqual(self.calc.divide(10, -2), -5.0, "10 / -2 should equal -5.0")
        self.assertEqual(self.calc.divide(0, 5), 0.0, "0 / 5 should equal 0.0")
        self.assertEqual(self.calc.divide(5.0, 2), 2.5, "5.0 / 2 should equal 2.5")
        self.assertIsNone(self.calc.divide(10, 0), "10 / 0 should return None")

if __name__ == "__main__":
    unittest.main()
