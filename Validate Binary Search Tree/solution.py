# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = None
        if not root:
            return True
        stack = [(root, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                stack.append((node, 1,))
                if node.left:
                    stack.append((node.left, 0,))
            elif state == 1:
                if node.right:
                    stack.append((node.right, 0,))
                if prev == None or prev < node.val:
                    prev = node.val
                else:
                    return False
        return True
