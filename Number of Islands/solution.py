
m collections import deque

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution(object):
    def floodfill(self, grid, visited, r, c):
        q = deque([(r, c,)])
        while len(q):
            t_r, t_c = q.popleft()
            if (t_r, t_c,) in visited:
                continue
            visited.add((t_r, t_c,))
            for d_r, d_c in direction:
                tt_r, tt_c = t_r + d_r, t_c + d_c
                if (tt_r, tt_c) not in visited and tt_r >=0 and tt_r < len(grid) and tt_c >=0 and tt_c < len(grid[0]) and grid[tt_r][tt_c] == '1':
                    q.append((tt_r, tt_c,))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j,) not in visited:
                    self.floodfill(grid, visited, i, j)
                    island_count += 1
        return island_count
        
