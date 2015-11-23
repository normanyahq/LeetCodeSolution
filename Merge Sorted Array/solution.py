class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tail = m+n-1
        if not n:
            return None
        if not m:
            nums1[:] = nums2[:]
            #assign each value, it may be wrong if you write:
            #nums1 = nums2
            return None
        m -= 1
        n -= 1

        while tail>=0:
            if m < 0 or n >= 0 and nums2[n] > nums1[m]:
                nums1[tail] = nums2[n]
                n -= 1
            else: # n < 0 or nums2 < nums1[m]
                nums1[tail] = nums1[m]
                m -= 1
            tail -= 1

