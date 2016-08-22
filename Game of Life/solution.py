class Solution(object):
    def checkLive(self, board, r, c):
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]
        count_live = 0
        row = len(board)
        if row:
            col = len(board[0])
        for dr, dc in dx:
            if r + dr >= 0 and r + dr < row and c + dc >=0 and c + dc < col:
                count_live += board[r + dr][c + dc] & 1
        return 1 if board[r][c] and count_live >= 2 and count_live <= 3 or count_live == 3 else 0
        
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row:
            col = len(board[0])
        for i in range(row):
            for j in range(col):
                board[i][j] |= self.checkLive(board, i, j) << 1
        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1
                
