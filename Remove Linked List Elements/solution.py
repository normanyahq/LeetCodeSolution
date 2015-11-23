# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            #t = head
            head = head.next
            #del t
            #python has GC, don't worry
        if not head or not head.next:
            return head
        last = head
        current = head.next
        while current:
            if current.val == val:
                last.next = current.next
                #t = current
                current = current.next
                #del t
            else:
                last = last.next
                current = current.next
        return head
