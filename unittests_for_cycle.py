import unittest
from cycle_1 import cycle


class TestCount(unittest.TestCase):
    def test_count(self):        
        result = next(cycle("ABCD"))                   
        self.assertEqual(result, "A")

if __name__ == 'main':
    unittest.main()
    
