class Sudoku:
    def __init__(self, grid):
        self.matrix = grid
    
    def find_next_empty(self):
        for row_index in range(len(self.matrix)):
            for column_index in range(len(self.matrix[row_index])):
                if self.matrix[row_index][column_index] == None:
                    return (row_index, column_index)

    def check_valid(self, number, row_index, column_index):
        row_invalid = self.check_in_row(number, row_index)
        column_invalid = self.check_in_column(number, column_index)
        square_invalid = self.check_in_square(number, row_index, column_index)
        if not row_invalid and not column_invalid and not square_invalid:
            return True
        return False

    def check_in_row(self, number, row_index):
        for cell in self.matrix[row_index]:
            if cell == number:
                return True
        return False

    def check_in_column(self, number, column_index):
        for row in self.matrix:
            if row[column_index] == number:
                return True
        return False

    def construct_inner_matrix(self, row_index, column_index):
        inner_matrix_pos = (int(row_index / 3) , int(column_index / 3))
        inner_matrix_rows = self.matrix[ inner_matrix_pos[0] * 3 : (inner_matrix_pos[0] + 1) * 3 ]
        inner_matrix_final = []
        for row in inner_matrix_rows:
            stripped_row = row[ inner_matrix_pos[1] * 3 : (inner_matrix_pos[1] + 1) * 3]
            inner_matrix_final.append(stripped_row)
        return inner_matrix_final

    def check_in_square(self, number, row_index, column_index):
        inner_matrix = self.construct_inner_matrix(row_index, column_index)
        for row in inner_matrix:
            if number in row:
                return True
        return False

    def solve(self):
        # base case
            # finds next empty cell to target, returns None if no more empty cells
        next_empty = self.find_next_empty()
        if next_empty == None:
            print(self.matrix)
            return self.matrix

        # tries each number 1 to 9 in empty cell and if valid sets cell to number
        for number in range(1,10):
            # if number is valid for cell then set it to the number
            if self.check_valid(number, next_empty[0], next_empty[1]) == True:
                self.matrix[next_empty[0]][next_empty[1]] = number
                # recursion to check the number is valid for the rest of the grid
                    # if the rest of the grid can be completed with this number in the cell return the current matrix to parent call
                if self.solve() == self.matrix:
                    return self.matrix
                # otherwise, empty the cell of the number we just tried in case this level of recursion has to return false (no valid solutions)
                self.matrix[next_empty[0]][next_empty[1]] = None
        #if each number tried and none of them work - returns false to parent function call
        return False
        