from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, result_dict):
        if not node:
            return 0
        max_depth = 1
        if node.left:
            max_depth = max(self.dfs(node.left, result_dict) + 1, max_depth) 
        if node.right:
            max_depth = max(self.dfs(node.right, result_dict) + 1, max_depth) 
        result_dict[max_depth].append(node.val)
        return max_depth
        
        
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        result_dict = defaultdict(list)
        max_depth = self.dfs(root, result_dict)
        for d in xrange(1, max_depth + 1):
            result.append(result_dict[d])
            max_depth += 1
        return result
