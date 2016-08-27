# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random 

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        p = self.head
        count = 1
        val = None
        while p:
            r = random.randint(0, count-1) 
            if not r:
                val = p.val
            p = p.next
            count += 1
        return val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
