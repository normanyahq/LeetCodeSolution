from collections import deque
class Solution(object):
    def isValidParentheses(self, s):
        l_count = 0
        for c in s:
            if c == "(":
                l_count += 1
            elif c == ")":
                l_count -= 1
                if l_count < 0:
                    return False
        return not l_count
    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        min_remove = len(s)
        q = deque([(s, 0)])
        visited = set([s])
        result = list()
        while q:
            t, depth = q.popleft()
            if depth > min_remove:
                break
            if self.isValidParentheses(t):
                min_remove = depth
                result.append(t)
            for i in xrange(len(t)):
                tt = t[:i] + t[i+1:]
                if tt not in visited:
                    visited.add(tt)
                    q.append((tt, depth+1))
        return resultw
