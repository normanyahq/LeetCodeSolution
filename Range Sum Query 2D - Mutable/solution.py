class StupidSum:
    def update(self, pos, val):
        pos += 1
        for i in xrange(pos, self.size):
            self.sums[i] += val

    def query(self, pos):
        pos += 1
        return self.sums[pos]

    def __init__(self, row):
        self.size = len(row) + 1
        self.sums = [0] * self.size
        for i in xrange(len(row)):
            self.sums[i+1] = self.sums[i] + row[i]


class BinaryIndexTree:
    def update(self, pos, val):
        pos += 1
        while pos < self.size:
            self.sums[pos] += val
            pos += pos & (-pos)

    def query(self, pos):
        pos += 1
        s = 0
        while pos:
            s += self.sums[pos]
            pos -= pos & (-pos)
        return s

    def __init__(self, row):
        self.size = len(row) + 1
        self.sums = [0] * self.size
        for i in xrange(len(row)):
            self.update(i, row[i])


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.sums = list()
        self.matrix = matrix
        for row in matrix:
            self.sums.append(StupidSum(row))

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
        self.sums[row].update(col, delta)


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = 0
        for i in xrange(row1, row2+1):
            s += self.sums[i].query(col2) - self.sums[i].query(col1-1)
        return s
