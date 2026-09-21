class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                square_position = (i //3) * 3 + (j // 3)
                if i in rows[val] or j in cols[val] or square_position in squares[val]:
                    return False
                rows[val].append(i)
                cols[val].append(j)
                squares[val].append(square_position)
        return True