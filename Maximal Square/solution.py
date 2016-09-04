from collections import defaultdict
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        f = defaultdict(int)
        max_len = 0
        for i in range(row):
            f[i, 0] = 1 if matrix[i][0] == '1' else 0
            max_len = max(max_len, f[i, 0])
        for i in range(col):
            f[0, i] = 1 if matrix[0][i] == '1' else 0
            max_len = max(max_len, f[0, i])

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    f[i, j] = min(f[i-1, j-1], f[i, j-1], f[i-1, j]) + 1
                    max_len = max(max_len, f[i, j])

        return max_len ** 2

