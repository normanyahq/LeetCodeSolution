# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val == q.val:
            return p
        if p.val == root.val or q.val == root.val:
            return root
        if (root.val > p.val) == (root.val > q.val):
            return self.lowestCommonAncestor(root.left if root.val > p.val else root.right, p, q)
        else:
            return root

        
