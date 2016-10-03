# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        t = self.dfs(root.left)
        if root.right and (root.right.left or root.right.right):
            t += self.dfs(root.right)
        return t
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or not root.left and not root.right:
            return 0
        return self.dfs(root)
