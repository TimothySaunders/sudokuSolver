import unittest
from src.sudoku import Sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.grid = [
            [None, None, None, 2, 6, None, 7, None, 1],
            [6, 8, None, None, 7, None, None, 9, None],
            [1 ,9, None, None, None, 4, 5, None, None],
            [8, 2, None, 1, None, None, None, 4, None],
            [None, None, 4, 6, None, 2, 9, None, None],
            [None, 5, None, None, None, 3, None, 2, 8],
            [None, None, 9, 3, None, None, None, 7, 4],
            [None, 4, None, None, 5, None, None, 3, 6],
            [7, None, 3, None, 1, 8, None, None, None]
        ]
        self.doku = Sudoku(self.grid)

    def test_find_none(self):
        self.assertEqual((0, 0), self.doku.find_next_empty())

    def test_find_none_v2(self):
        grid = [
            [5, 9, 6, 2, 6, 7, 7, 8, 1],
            [6, 8, 6, None, 7, None, None, 9, None],
            [1 ,9, None, None, None, 4, 5, None, None],
            [8, 2, None, 1, None, None, None, 4, None],
            [None, None, 4, 6, None, 2, 9, None, None],
            [None, 5, None, None, None, 3, None, 2, 8],
            [None, None, 9, 3, None, None, None, 7, 4],
            [None, 4, None, None, 5, None, None, 3, 6],
            [7, None, 3, None, 1, 8, None, None, None]
        ]
        self.doku_2 = Sudoku(grid)
        self.assertEqual((1, 3), self.doku_2.find_next_empty())

    def test_check_in_row_true(self):
        self.assertEqual(True, self.doku.check_in_row(2, 0))

    def test_check_in_row_false(self):
        self.assertEqual(False, self.doku.check_in_row(3, 0))

    def test_check_in_column_true(self):
        self.assertEqual(True, self.doku.check_in_column(1, 0))

    def test_check_in_column_false(self):
        self.assertEqual(False, self.doku.check_in_column(4, 0))

    def test_check_in_square_true(self):
        self.assertEqual(True, self.doku.check_in_square(6, 0, 0))

    def test_check_in_square_false(self):
        self.assertEqual(False, self.doku.check_in_square(8, 6, 6))

    def test_construct_inner_matrix_0_0(self):
        self.assertEqual([[None, None, None], [6, 8, None], [1, 9, None]], self.doku.construct_inner_matrix(1, 1))

    def test_construct_inner_matrix_2_2(self):
        self.assertEqual([[None, None, None], [6, 8, None], [1, 9, None]], self.doku.construct_inner_matrix(2, 2))

    def test_construct_inner_matrix_3_3(self):
        self.assertEqual([[1, None, None], [6, None, 2], [None, None, 3]], self.doku.construct_inner_matrix(3, 3))       
        
    def test_check_valid_true(self):
        self.assertEqual(True, self.doku.check_valid(5, 0, 0))

    def test_check_valid_false(self):
        self.assertEqual(False, self.doku.check_valid(8, 0, 0))
    
    def test_solve(self):
        solution = [
            [4, 3, 5, 2, 6, 9, 7, 8, 1],
            [6, 8, 2, 5, 7, 1, 4, 9, 3],
            [1, 9, 7, 8, 3, 4, 5, 6, 2],
            [8, 2, 6, 1, 9, 5, 3, 4, 7],
            [3, 7, 4, 6, 8, 2, 9, 1, 5],
            [9, 5, 1, 7, 4, 3, 6, 2, 8],
            [5, 1, 9, 3, 2, 6, 8, 7, 4],
            [2, 4, 8, 9, 5, 7, 1, 3, 6],
            [7, 6, 3, 4, 1, 8, 2, 5, 9]]
        self.assertEqual(solution, self.doku.solve())