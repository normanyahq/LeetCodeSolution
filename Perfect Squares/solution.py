from collections import deque
from math import sqrt
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = deque()
        q.append((n, 0,))
        visited = set([n])
        while len(q):
            num, step = q.popleft()
            if num == 0 or int(sqrt(num)) ** 2 == num:
                return step + 1

            i = int(sqrt(num))
            while i*i < num:
                if not num-i*i in visited:
                    q.append((num - i*i, step+1,))
                    visited.add(num - i*i)
                i -= 1
