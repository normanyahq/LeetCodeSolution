# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #define elements in stack: (node, depth, state)
        # state = 0: not visited
        #       = 1: visited left child
        #       = 2: visited right child
        min_depth = -1
        if not root:
            return 0
        stack = [(root, 1, 0)]
        while stack:
            node, depth, state = stack.pop()
            if not node.left and not node.right:
                if min_depth == -1 or depth < min_depth:
                    min_depth = depth
                    
                    
            if state == 0:
                stack.append((node, depth, 1))
                if node.left:
                    stack.append((node.left, depth+1, 0))
            if state == 1:
                if node.right:
                    stack.append((node.right, depth+1, 0))
                    
        return min_depth    
        
