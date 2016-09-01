from collections import deque
class Solution(object):
    def get_min_dist(self, grid, row, col, count, cur_min):
        visited = set([(row, col)])
        q = deque([(row, col, 0)])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = 0
        while q and count:
            r, c, depth = q.popleft()
            if grid[r][c] == 1:
                count -= 1
                dist += depth
                if dist >= cur_min:
                    return cur_min
            elif not grid[r][c]:
                for dr, dc in dx:
                    tr, tc = r+dr, c+dc
                    if tr >= 0 and tc >=0 and tr < len(grid) and tc < len(grid[0]) and grid[tr][tc] < 2 and (tr, tc) not in visited:
                        q.append((tr, tc, depth + 1))
                        visited.add((tr, tc))
        if count:
            for r, c in visited:
                if grid[r][c] == 0:
                    grid[r][c] = 2 
            return -1
        return dist
                
        
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        n_building = 0
        for r in grid:
            for g in r:
                if g == 1:
                    n_building += 1
        row = len(grid)
        col = len(grid[0])
        min_dist = float('Inf')
        
        for r in xrange(row):
            for c in xrange(col):
                if grid[r][c] == 0:
                    dist = self.get_min_dist(grid, r, c, n_building, min_dist)
                    if dist == -1:
                        continue
                    min_dist = min(dist, min_dist)
        return min_dist if min_dist < float('Inf') else -1
                
        
