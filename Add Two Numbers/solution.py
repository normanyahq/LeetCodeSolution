# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        overflow = 0
        p1 = l1
        p2 = l2
        head = ListNode(0)
        p3 = None
        while p1 or p2:
            if not p3:
                p3 = head
            else:
                p3.next = ListNode(overflow)
                p3 = p3.next
            p3.val += (p1.val if p1 else 0) + (p2.val if p2 else 0)
            overflow = p3.val / 10
            p3.val %= 10
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        if overflow:
            p3.next = ListNode(overflow)
        return head
            
