# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to
# be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in rows[i] \
                        or board[i][j] in cols[j] \
                        or board[i][j] in boxes[(i // 3, j // 3)]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i // 3, j // 3)].add(board[i][j])
        return True



