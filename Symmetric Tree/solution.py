# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        #definition for tuple: (left, right, state)
        # state = 0: not checked
        # state = 1: checked sub tree left->left with left->right
        # state = 2: finish check, in this case, we don't need to push the tuple into stack
        stack.append((root.left, root.right, 0))
        while stack:
            left, right, state = stack.pop()
            if (not left and not right):
                continue
            if (not left and right) or (not right and left) or (left.val != right.val):
                return False
            if state == 0:
                stack.append((left, right, 1))
                stack.append((left.left, right.right, 0))
            if state == 1:
                stack.append((left.right, right.left, 0))
        return True
