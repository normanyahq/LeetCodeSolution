import heapq, time
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def getLen(l, r):
            return max(0, r-l+1)

        def findKthInSortedArrays(arr1, l1, r1, arr2, l2, r2, k):
            if getLen(l1, r1) < getLen(l2, r2):
                arr1, l1, r1, arr2, l2, r2 = arr2, l2, r2, arr1, l1, r1
            if not getLen(l2, r2):
                return arr1[l1 + k]
            if k == getLen(l1, r1) + getLen(l2, r2) - 1:
                return max(arr1[r1], arr2[r2])
            mid1 = (r1 + l1) / 2
            mid2 = (r2 + l2) / 2
            if k < getLen(l2, mid2) + getLen(l1, mid1) - 1:
                if arr1[mid1] < arr2[mid2]:
                    return findKthInSortedArrays(arr1, l1, r1, arr2, l2, mid2-1, k)
                else:
                    return findKthInSortedArrays(arr1, l1, mid1-1, arr2, l2, r2, k)
            else:
                if arr1[mid1] < arr2[mid2]:
                    return findKthInSortedArrays(arr1, mid1+1, r1, arr2, l2, r2, k - getLen(l1, mid1))
                else:
                    return findKthInSortedArrays(arr1, l1, r1, arr2, mid2+1, r2, k - getLen(l2, mid2))


        n = len(nums1) + len(nums2)
        if n % 2:
            return findKthInSortedArrays(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, n // 2)
        else:
            return (findKthInSortedArrays(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, n // 2) + findKthInSortedArrays(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, n // 2 - 1)) / 2.

