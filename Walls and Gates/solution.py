from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        row = len(rooms)
        if row:
            col = len(rooms[0])
        for i in range(row):
            for j in range(col):
                if not rooms[i][j]:
                    q = deque()
                    dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dr, dc in dx:
                        if i + dr < row and i + dr >= 0 and j + dc < col and j + dc >= 0 and rooms[i + dr][j + dc] > 0:
                            q.append((i+dr, j+dc, 1))

                    while q:
                        r, c, depth = q.popleft()
                        if rooms[r][c] > depth:
                            rooms[r][c] = depth
                        for dr, dc in dx:
                            if r + dr < row and r + dr >= 0 and c + dc < col and c + dc >= 0 and rooms[r + dr][c + dc] > depth + 1:
                                q.append((r+dr, c+dc, depth + 1))


                            
                            
