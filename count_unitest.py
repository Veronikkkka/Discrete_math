import unittest
from itertools_count import count


class TestCount(unittest.TestCase):
    def test_count(self):
        value = count(4, 5)
        first = next(value)
        second = next(value)
        result = [first, second]
        self.assertEqual(result, [4, 9])


if __name__ == '__main__':
    unittest.main()
