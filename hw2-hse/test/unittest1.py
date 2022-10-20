def open_file():
    file = input('Введите название файла: ')
    with open(file,'r') as f:
        a = [int(i) for i in f.read().splitlines()[0].split()]
    return a
def _mult(a):
    answer = 1
    for i in range(len(a)):
        answer = answer * a[i]
    return answer

a = open_file()
import unittest
import math
class test_area(unittest.TestCase):
    def test_mult(self):
        res = _mult(a)
        self.assertEqual(res,math.prod(a))
if __name__ == '__main__':
    unittest.main()