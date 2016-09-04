from collections import defaultdict
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        horizontal = [[0] * col for i in xrange(row)]
        vertical = [[0] * col for i in xrange(row)]
        empty_slot = []
        for i in xrange(row):
            cnt = 0
            for j in range(col):
                if grid[i][j] == 'E':
                    cnt += 1
                elif grid[i][j] == 'W':
                    cnt = 0
                else:
                    empty_slot.append((i,j))
                horizontal[i][j] = cnt
            cnt = 0
            for j in xrange(col-1, -1, -1):
                if grid[i][j] == 'E':
                    cnt += 1
                elif grid[i][j] == 'W':
                    cnt = 0
                horizontal[i][j] += cnt - (grid[i][j] == 'E')
        for j in xrange(col):
            cnt = 0
            for i in xrange(row):
                if grid[i][j] == 'E':
                    cnt += 1
                elif grid[i][j] == 'W':
                    cnt = 0
                vertical[i][j] = cnt
            cnt = 0
            for i in xrange(row-1, -1, -1):
                if grid[i][j] == 'E':
                    cnt += 1
                elif grid[i][j] == 'W':
                    cnt = 0
                vertical[i][j] += cnt - (grid[i][j] == 'E')
        result = 0
        for i, j in empty_slot:
            result = max(result, vertical[i][j] + horizontal[i][j])
        return result

