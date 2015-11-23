class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.partialSum = []
        if len(nums):
            self.partialSum.append(nums[0])
        for i in range(1, len(nums)):
            self.partialSum.append(self.partialSum[i-1] + nums[i])
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.partialSum[j] - (self.partialSum[i-1] if i else 0)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
