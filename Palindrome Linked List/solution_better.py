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
        if not head or not head.next:
            return True
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            t = slow
            slow = slow.next
            t.next = None
        slow = self.reverseLinkedList(slow)
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
    def reverseLinkedList(self, head):
        last = head
        current = head.next
        head.next = None
        while current:
            t = current.next
            current.next = last
            last = current
            current = t
        return last
        
