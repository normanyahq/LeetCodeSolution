# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        last, current, next = None, head, head.next
        while current:
            next = current.next
            current.next = last
            last = current
            current = next
            
        return last

        
