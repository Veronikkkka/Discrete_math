import unittest
from project_combi import combinations


class TestCombinations(unittest.TestCase):
    def test_combinations(self):
        self.assertEqual(list(combinations('ABCD', 3)), [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')])

    def test_combinations(self):
        self.assertEqual(list(combinations(['K', 'A', 'T', 'E'], 4)), [('K', 'A', 'T', 'E')])

    def test_combinations(self):
        self.assertEqual(list(combinations(['B', 'R', 'E', 'N', 'D', 'I'], 7)), [])

    def test_combinations(self):
        self.assertEqual(len(list(combinations(['B', 'R', 'E', 'N', 'D', 'I'], 7))), 0)

if __name__ == 'main':
    unittest.main()