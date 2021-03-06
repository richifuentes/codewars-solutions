import unittest

import array_diff2

class TestArrayDiff(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual(array_diff2.array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEqual(array_diff2.array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEqual(array_diff2.array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEqual(array_diff2.array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEqual(array_diff2.array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")


if __name__ == '__main__':
    unittest.main()
