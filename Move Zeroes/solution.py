class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z_pos = 0 # the position of first zero
        nz_pos = 0 # the position of first non-zero number after the first zero
        while z_pos < len(nums) and nz_pos < len(nums):
            while z_pos < len(nums) and nums[z_pos]:
                z_pos += 1
            nz_pos = z_pos + 1
            while nz_pos < len(nums) and not nums[nz_pos]:
                nz_pos += 1
            if nz_pos < len(nums):
                nums[z_pos], nums[nz_pos] = nums[nz_pos], nums[z_pos]
            
                
        
        
            
