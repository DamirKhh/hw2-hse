from main import _mult,_sum,_min,_max
a = [int(i) for i in open('/home/runner/work/hw2-hse/hw2-hse/t5.txt').readline().split()]
import unittest
import math
class test_area(unittest.TestCase):
    def test_mult(self):
        res = _mult(a)
        self.assertEqual(res,math.prod(a))
    def test_sum(self):
        res = _sum(a)
        self.assertEqual(res,sum(a))
    def test_max(self):
        res = _max(a)
        self.assertEqual(res,max(a))
    def test_min(self):
        res = _min(a)
        self.assertEqual(res,min(a))
if __name__ == '__main__':
    unittest.main()
