import unittest
import sys
sys.path.append(".")

from Matrix_from_file import read_matrix
from Matrix_from_file import close_file

class Testing(unittest.TestCase):

    def test_fromFile(self):      #matrix_from_file test
        expected = [[1.0, 2.0, 3.0, 5.0], [3.0, 4.0, 5.0, 2.0], [5.55, 6.0, 7.0, 1.0], [8.0, 9.0, 10.0, 1.0], [1.0, 2.0, 3.0, 5.0]]
        matrix = read_matrix('macierz.txt')
        self.assertEqual(expected, matrix)



if __name__ == '__main__':        #begin the tests
    unittest.main()
