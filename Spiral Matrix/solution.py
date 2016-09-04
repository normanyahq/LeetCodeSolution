class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return list()
        dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dx_p = 0
        row = len(matrix)
        col = len(matrix[0])
        r, c = 0, 0
        result = list()
        visited = set()
        for i in range(row * col):
            result.append(matrix[r][c])
            visited.add((r, c))
            while i != row * col - 1:
                tr, tc = r + dx[dx_p][0], c + dx[dx_p][1]
                if tr >=0 and tr < row and tc >= 0 and tc < col and (tr, tc) not in visited:
                    r, c = tr, tc
                    break
                else:
                    dx_p = (dx_p + 1) % 4
        return result
