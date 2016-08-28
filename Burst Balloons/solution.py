class Solution(object):
    def __init__(self):
        self.cache = dict()
    
    def dp(self, i, j):
        if i >= j:
            return 0
        elif (i, j) in self.cache:
            return self.cache[i, j]
        else:
            max_v = 0
            for k in range(i+1, j):
                v = self.dp(i, k) + self.dp(k, j) + self.w[i] * self.w[j] * self.w[k]
                if max_v < v:
                    max_v = v
            self.cache[i, j] = max_v
        return self.cache[i, j]
    
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 1)
        nums.append(1)
        self.w = nums
        return self.dp(0, len(nums) - 1)
