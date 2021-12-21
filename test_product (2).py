import unittest
from product import product


class TestProduct(unittest.TestCase):

    def test_product(self):
        self.assertEqual(list(product('AB', '12', '1')), \
[('A', '1', '1'), ('A', '2', '1'), ('B', '1', '1'), ('B', '2', '1')])
        self.assertEqual(list(product()), [()])
        self.assertEqual(list(product('AB')), [('A',), ('B',)])
        self.assertEqual(list(product('A', '1')), [('A', '1')])
        self.assertEqual(list(product('AB', repeat=2)), \
[('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')])
        self.assertEqual(len(list(product('00', repeat=10))), 1024)
        self.assertEqual(len(list(product('00', repeat=20))), 2 ** 20)
        self.assertEqual(list(product(1, 23)), [('1', '2'), ('1', '3')])


if __name__ == '__main__':
    unittest.main()
