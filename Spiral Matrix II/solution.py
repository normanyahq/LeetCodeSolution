class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in range(n)]
        r, c = 0, 0
        dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dx_p = 0
        for i in range(n * n):
            matrix[r][c] = i + 1
            tr, tc = r + dx[dx_p][0], c + dx[dx_p][1]
            while i != n * n - 1:
                tr, tc = r + dx[dx_p][0], c + dx[dx_p][1]
                if tr >=0 and tr < n and tc >= 0 and tc < n and not matrix[tr][tc]:
                    r, c = tr, tc
                    break
                else:
                    dx_p = (dx_p + 1) % 4
        return matrix
        
