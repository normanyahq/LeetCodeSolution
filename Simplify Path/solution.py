from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        q = deque()
        path = path.split('/')
        for f in path:
            if f == "..":
                if q:
                    q.pop()
            elif f != "." and f:
                q.append(f)
        result = "/" + (q.popleft() if q else "")
        while q:
            result += "/" + q.popleft()
        return result
