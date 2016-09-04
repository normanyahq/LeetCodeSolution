# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        stack = list()
        while p.next:
            stack.append(p)
            p = p.next
        p.val = (p.val + 1) % 10
        if not p.val:
            while stack:
                t = stack.pop()
                t.val = (t.val + 1) % 10
                if t.val:
                    break
        if head.val == 0:
            t = ListNode(1)
            t.next = head
            head = t
        
        return head
                
        
