from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj_list = defaultdict(set)
        max_depth = 0
        if not edges:
            return [i for i in range(n)]
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
            
        cur = list()
        for i in adj_list:
            if len(adj_list[i]) == 1:
                cur.append(i)
        while True:
            next = list()
            for node in cur:
                for v in adj_list[node]:
                    adj_list[v].remove(node)
                    if len(adj_list[v]) == 1:
                        next.append(v)
            if not next:
                return cur
            else:
                cur = next

