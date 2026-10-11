class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                box_num = (i//3)*3 + j//3
                if board[i][j] in box_set[box_num] or board[i][j] in row_set[i] or board[i][j] in col_set[j]:
                    return False
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                box_set[box_num].add(board[i][j])
        return True