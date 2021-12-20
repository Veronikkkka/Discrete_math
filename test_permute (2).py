import unittest
from permutations import permutations


class TestCombinations(unittest.TestCase):
    def test_combinations(self):
        self.assertEqual(list(permutations('ABCD', 3)), [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')])
    
    def test_combinations(self):
        self.assertEqual(list(permutations(['K', 'A', 'T', 'E'], 4)), [('K', 'A', 'T', 'E'), ('K', 'A', 'E', 'T'), ('K', 'T', 'A', 'E'), ('K', 'T', 'E', 'A'), ('K', 'E', 'A', 'T'), ('K', 'E', 'T', 'A'), ('A', 'K', 'T', 'E'), ('A', 'K', 'E', 'T'), ('A', 'T', 'K', 'E'), ('A', 'T', 'E', 'K'), ('A', 'E', 'K', 'T'), ('A', 'E', 'T', 'K'), ('T', 'K', 'A', 'E'), ('T', 'K', 'E', 'A'), ('T', 'A', 'K', 'E'), ('T', 'A', 'E', 'K'), ('T', 'E', 'K', 'A'), ('T', 'E', 'A', 'K'), ('E', 'K', 'A', 'T'), ('E', 'K', 'T', 'A'), ('E', 'A', 'K', 'T'), ('E', 'A', 'T', 'K'), ('E', 'T', 'K', 'A'), ('E', 'T', 'A', 'K')])

    def test_combinations(self):
        self.assertEqual(list(permutations(['B', 'R', 'E', 'N', 'D', 'I'], 7)), [])

if __name__ == 'main':
    unittest.main()