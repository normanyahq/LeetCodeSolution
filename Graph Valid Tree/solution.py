from collections import defaultdict, deque
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adj_list = defaultdict(list)
        for s, t in edges:
            adj_list[s].append(t)
            adj_list[t].append(s)
        
        if not n:
            return not len(edges)
        if not edges:
            return n == 1
        q = deque([(-1, edges[0][0])])
        added = set([edges[0][0]])
        while q:
            prev, s = q.popleft()
            for t in adj_list[s]:
                if t in added:
                    if t != prev:
                        return False
                else:
                    added.add(t)
                    q.append((s, t))
        return len(added) == n
            
        
