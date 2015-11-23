# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length_A = 0
        length_B = 0
        if not headA or not headB:
            return None
        t = headA
        while t:
            length_A += 1
            t = t.next
        t = headB
        while t:
            length_B += 1
            t = t.next
        tA, tB = headA, headB
        if length_A > length_B:
            for i in range(0, length_A - length_B):
                tA = tA.next
        elif length_B > length_A:
            for i in range(0, length_B - length_A):
                tB = tB.next
        while tA and tB:
            if tA == tB:
                return tA
            tA = tA.next
            tB = tB.next
        return tA
