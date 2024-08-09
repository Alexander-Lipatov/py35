import inc_dec    # The code to test
import unittest   # The test framework
from main import IntNumbers

class TestIntNumbers(unittest.TestCase):
    def test_sum_el(self):
        kit = IntNumbers(1,2,3)
        self.assertEqual(kit.sum_el(), 6, '6')
        self.assertEqual(kit.max_el(), 6, '6')
        self.assertEqual(kit.sum_el(), 6, '6')
        self.assertEqual(kit.sum_el(), 6, '6')



if __name__ == '__main__':
    unittest.main()
