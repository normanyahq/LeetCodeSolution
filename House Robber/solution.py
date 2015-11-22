class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return max(nums + [0]) # deal with empty list
        #f [i, rob_i] means the max amount for the first i houses,
        # if we rob the ith house (rob_i == True) or not (rob_i == False)
        f = {(0, True,): nums[0], 
                    (0, False,): 0,
                    (1, True,): nums[1],
                    (1, False,): nums[0]}
        for i in range(2, len(nums)):
            f[(i, True,)] = max(f[i-2, True] + nums[i], f[i-2, False] + nums[i], f[i-1, False])
            f[(i, False,)] = max(f[i-2, True], f[i-1, True])
        return max (f[len(nums)-1, True], f[len(nums)-1, False])
