class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #python magic zip
        for l in board + zip(*[list(l) for l in board]):
            if len(l) - l.count('.') != len(set(l)) - ('.' in set(l)):
                return False
        for i in range(0, 3):
            for j in range(0, 3):
                t = ""
                for k in range(0, 3):
                    t += "".join(board[i*3 + k][j*3 : j*3+3])
                if len(t) - t.count('.')  != len(set(t)) - ('.' in set(t)):
                    return False
        return True
