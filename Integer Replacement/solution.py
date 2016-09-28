from collections import deque
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = deque([(n, 0)])
        visited = set()
        visited.add(n)
        while q:
            v, d = q.popleft()
            if v == 1:
                return d
            if v % 2:
                if v + 1 not in visited:
                    q.append((v + 1, d + 1))
                if v - 1 not in visited:
                    q.append((v - 1, d + 1))
            else:
                if v / 2 not in visited:
                    q.append((v / 2, d + 1))
                    visited.add(v / 2)
        
                
        
