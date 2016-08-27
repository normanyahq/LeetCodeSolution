from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.max_size = size
        self.q = deque()
        self.s = 0.

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) == self.max_size:
            self.s -= self.q.popleft()
        self.s += val
        self.q.append(val)
        return self.s / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
