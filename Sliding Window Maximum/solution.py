from collections import deque
class MaxDeque:
    def __init__(self):
        self.q = deque()
        self.max_q = deque()
    
    def push(self, v):
        while self.max_q and v > self.max_q[-1]:
            self.max_q.pop()
        self.max_q.append(v)
        self.q.append(v)
    
    def pop(self):
        t = self.q.popleft()
        if t == self.max_q[0]:
            self.max_q.popleft()
        return t
    
    def getMax(self):
        return self.max_q[0]
            

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return list()
        q = MaxDeque()
        for i in range(min(k, len(nums))):
            q.push(nums[i])
        i = k
        result = [q.getMax()]
        while i < len(nums):
            q.pop()
            q.push(nums[i])
            result.append(q.getMax())
            i += 1
        return result
        
            
