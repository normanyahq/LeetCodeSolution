from collections import defaultdict

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        k = 3
        f = defaultdict(int)
        if not costs:
            return 0
        color_num = len(costs[0])

        for i in range(len(costs[0])):
            f[0, i] = costs[0][i]
        for i in range(1, len(costs)):
            for j in range(color_num):
                for k in range(color_num):
                    if j == k:
                        continue
                    if (i, j) not in f or f[i, j] > f[i-1, k] + costs[i][j]:
                        f[i, j] = f[i-1, k] + costs[i][j]
        result = float('Inf')
        for i in range(color_num):
            result = min(f[len(costs) - 1, i], result)
        return result
        
