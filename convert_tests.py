import unittest
from convert import str_to_float


class TestCases(unittest.TestCase):
    # task 1
    def test_float_str(self):
        self.assertEqual(str_to_float("3.14"), 3.14)
        self.assertEqual(str_to_float("0.001"), 0.001)
        self.assertEqual(str_to_float("100"), 100.0)

    def test_float_str_2(self):
        self.assertIsNone(str_to_float("abc"))
        self.assertIsNone(str_to_float(""))
        self.assertIsNone(str_to_float("3.14abc"))

if __name__ == "__main__":
    unittest.main()
