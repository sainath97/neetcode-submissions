class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            self.prefix_matrix[i][0] = matrix[i][0]
            for j in range(1, cols):
                self.prefix_matrix[i][j] = self.prefix_matrix[i][j - 1] + matrix[i][j]
        print(self.prefix_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            print((i, col1, col2))
            sum += self.prefix_matrix[i][col2] if col1 == 0 else self.prefix_matrix[i][col2] - self.prefix_matrix[i][col1-1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)