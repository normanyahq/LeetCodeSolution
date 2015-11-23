# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        values = []
        t = head
        while t:
            values.append(t.val)
            t = t.next
        return sum (map(lambda x: abs(x[0] - x[1]), zip(values, reversed(values)))) == 0
