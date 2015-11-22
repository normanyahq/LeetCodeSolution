# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = head
        while t:
            while t.next and t.val == t.next.val:
                temp = t.next
                t.next = temp.next
                del temp # not necessary for python, but critical to C/C++
            t = t.next
        return head
