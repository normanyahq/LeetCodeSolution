from collections import deque
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        max_x, min_x, max_y, min_y = x, x, y, y
        row = len(image)
        if row:
            col = len(image[0])
        visited = set([(x, y)])
        q = deque([(x, y)])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            min_x = min(min_x, r)
            max_x = max(max_x, r)
            min_y = min(min_y, c)
            max_y = max(max_y, c)
            for dr, dc in dx:
                tr, tc = dr + r, dc + c
                if tr>=0 and tr<row and tc>=0 and tc<col and image[tr][tc] == '1' and (tr, tc) not in visited:
                    visited.add((tr, tc))
                    q.append((tr, tc))
        return (max_x - min_x + 1) * (max_y - min_y + 1)
            
            
        
