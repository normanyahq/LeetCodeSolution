# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        p = None
        heap = list()
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, node, i))

        while heap:
            _, node, i = heapq.heappop(heap)
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i], i))
            if not head:
                head = node
                p = head
                p.next = None
            else:
                p.next = node
                node.next = None
                p = node
        return head
                
                
