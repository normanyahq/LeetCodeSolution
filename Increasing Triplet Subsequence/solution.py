class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = [None] * 3
        for n in nums:
            print arr
            for i in xrange(3):
                if arr[i] == None or arr[i] > n:
                    arr[i] = n
                    break
                elif arr[i] == n:
                    break
            if i == 2 and arr[i] != None:
                return True
            
        return False
        

