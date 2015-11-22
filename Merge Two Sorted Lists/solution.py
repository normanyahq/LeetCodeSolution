# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pos1, pos2 = 0, 0
        result = []
        if not l1 or not l2:
            return l1 if not l2 else l2
        while l1 or l2:
            if not l1 or l2 and l1.val > l2.val: #corner case! Remember!
                result.append(l2.val)
                l2 = l2.next
            else:
                result.append(l1.val)
                l1 = l1.next
        return result
