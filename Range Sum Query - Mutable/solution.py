class BinaryIndexTree():
    def __init__(self, arr):
        self.size = (len(arr) + 1)
        self.sums = [0] * self.size
        for i in xrange(len(arr)):
            self.update(i, arr[i])
    
    def update(self, pos, delta):
        pos += 1
        while pos < self.size:
            self.sums[pos] += delta
            pos += pos & (-pos)
            
    def query(self, pos):
        pos += 1
        return_val = 0
        while pos:
            return_val += self.sums[pos]
            pos -= pos & (-pos)
        return return_val

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = BinaryIndexTree(nums)
        self.nums = nums
        
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.sums.update(i, val - self.nums[i])
        self.nums[i] = val
        
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums.query(j) - self.sums.query(i-1)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
