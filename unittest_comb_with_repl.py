import unittest
from combinations_with_replacement import combinations_with_replacement
class TestCombWithRepl(unittest.TestCase):
    def test_combinations_with_replacement1(self):
        self.assertEqual(list(combinations_with_replacement([1], 4)), [(1, 1, 1, 1)])
    def test_combinations_with_replacement2(self):
        self.assertEqual(list(combinations_with_replacement([1, 5], 3)), [(1, 1, 1), (1, 1, 5), (1, 5, 5), (5, 5, 5)])
    def test_combinations_with_replacement3(self):
        self.assertEqual(list(combinations_with_replacement('ABC', 2)), [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')])
if __name__ == 'main':
    unittest.main()