import unittest
from repeat import repeat
class TestRepeat(unittest.TestCase):
    def test_repeat(self):
        result = list(next(repeat('ABC')))
        self.assertEqual(result, ['ABC'])
if __name__ == 'main':
    unittest.main()