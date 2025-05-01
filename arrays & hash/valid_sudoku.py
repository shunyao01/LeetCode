from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Check if the current fill cells in the sudoku board is valid

        Args:
            A 9x9 sudoku borad with string 1-9 and .

        Return:
            boolean: if the board is valid

        Time Complexity: O(n) where n is the number of square
        Space Complexity: O(1)

        Tricks: Use hashmap to track unique value, 1 set for 1 row, 1 set for 1 col
        """
        n = 9

        def check_unit(get_cell) -> bool:
            """
            Check if the row or column or box given the input is valid 

            Args:
                get_cell: a function (accessor) to be called to retrieve cell value
            """
            seen = [False] * 10
            for i in range(9):
                c = get_cell(i)
                if c != '.':
                    val = int(c)
                    if seen[val]:
                        return False
                    seen[val] = True
            return True

        # Check rows
        for i in range(9):
            if not check_unit(lambda j: board[i][j]):
                return False

        # Check columns
        for j in range(9):
            if not check_unit(lambda i: board[i][j]):
                return False

        # Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                if not check_unit(lambda k: board[box_row + k // 3][box_col + k % 3]):
                    return False

        return True

        # row_sets = [set() for _ in range(n)]
        # col_sets = [set() for _ in range(n)]
        # box_sets = [set() for _ in range(n)]

        # for i in range(n):
        #     for j in range(n):

        #         c = board[i][j]
        #         if c == '.': continue
        #         c = int(c)

        #         # check in respective set
        #         if c in row_sets[i]: return False
        #         if c in col_sets[j]: return False
        #         if c in box_sets[i//3*3 + j//3]: return False

        #         # add to sets
        #         row_sets[i].add(c)
        #         col_sets[j].add(c)
        #         box_sets[i//3*3 + j//3].add(c)

        # return True