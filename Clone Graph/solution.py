# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        q = deque([node])
        label_dict = dict()
        to_return = None
        while q:
            node = q.popleft()
            if node.label not in label_dict:
                label_dict[node.label] = UndirectedGraphNode(node.label)
                to_return = label_dict[node.label]
            for t in node.neighbors:
                if t.label not in label_dict:
                    label_dict[t.label] = UndirectedGraphNode(t.label)
                    q.append(t)
                label_dict[node.label].neighbors.append(label_dict[t.label])
        return to_return
                
