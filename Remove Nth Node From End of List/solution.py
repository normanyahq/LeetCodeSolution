# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for i in range(0, n):
            fast = fast.next
        last = None
        current = head
        while fast:
            last = current
            current = current.next
            fast = fast.next
        if last:
            last.next = last.next.next
        else:
            last = current.next
            head = last
        del current
        return head
            
