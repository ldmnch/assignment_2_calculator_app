import unittest
from geometry import Circle  

class TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), 3.14 * 5 * 5)

    def test_perimeter(self):
        c = Circle(5)
        self.assertAlmostEqual(c.perimeter(), 2 * 3.14 * 5)

if __name__ == "__main__":
    unittest.main()
