import unittest
from add import add
class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-2, 2), 0)
    def test_add_negative(self):
        self.assertNotEqual(add(2, 3), 6)
        self.assertNotEqual(add(0, 1), 0)
        self.assertNotEqual(add(-2, 2), -1)
if __name__ == '__main__':
    unittest.main()