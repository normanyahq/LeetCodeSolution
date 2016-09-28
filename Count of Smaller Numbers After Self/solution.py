class BinaryIndexTree:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.sums = [0] * self.capacity
    
    def update(self, pos, val):
        pos += 1
        while pos < self.capacity:
            self.sums[pos] += val
            pos += pos & (-pos)
    
    def query(self, pos):
        pos += 1
        s = 0
        while pos:
            s += self.sums[pos]
            pos -= pos & (-pos)
        return s

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        pos = {v: i for i, v in enumerate(sorted(nums))}
        tree = BinaryIndexTree(len(nums))
        for v in nums[::-1]:
            result.append(tree.query(pos[v]-1))
            tree.update(pos[v], 1)
        return list(reversed(result))
        
