class BinaryIndexTree2D:
    def update(self, row, col, val):
        row += 1
        col += 1
        while row < self.row:
            c = col
            while c < self.col:
                self.sums[row][c] += val
                c += c & (-c)
            row += row & (-row)

    def query(self, row, col):
        row += 1
        col += 1
        s = 0
        while row:
            c = col
            while c:
                s += self.sums[row][c]
                c -= c & (-c)
            row -= row & (-row)
        return s

    def __init__(self, matrix):
        self.row = len(matrix) + 1
        self.col = 0 if self.row == 1 else (len(matrix[0]) + 1)
        self.sums = [[0] * self.col for i in xrange(self.row)]
        self.matrix = matrix
        for i in xrange(self.row-1):
            for j in xrange(self.col-1):
                self.update(i, j, matrix[i][j])

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.sums = list()
        self.matrix = matrix
        self.sums = BinaryIndexTree2D(matrix)

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.sums.update(row, col, delta)


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums.query(row2, col2) + self.sums.query(row1-1, col1-1)\
            - self.sums.query(row1-1, col2) - self.sums.query(row2, col1-1)
