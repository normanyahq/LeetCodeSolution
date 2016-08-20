# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution(object):
    def __init__(self):
        self.result = 0

    def dfs(self, root, last_value, depth):
        if not root:
            return
        if depth > self.result:
            self.result = depth
        if last_value == root.val - 1:
            if depth + 1 > self.result:
                self.result = depth + 1
            self.dfs(root.left, root.val, depth + 1)
            self.dfs(root.right, root.val, depth + 1)
        else:
            self.dfs(root.left, root.val, 1)
            self.dfs(root.right, root.val, 1)
        
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root, None, 1)
        return self.result
        
