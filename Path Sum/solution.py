# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        #state = 0 -> not visited
        #        1 -> visited left child
        #        2 -> visited rigt child
        stack = [(root, 0, 0)]
        while stack:
            node, t_sum, state = stack.pop()
            if not node.left and not node.right:
                if t_sum + node.val == sum:
                    return True
                else:
                    continue
            if state == 0:
                stack.append((node, t_sum, 1))
                if node.left:
                    stack.append((node.left, t_sum + node.val, 0))
            elif state == 1:
                if node.right:
                    stack.append((node.right, t_sum + node.val, 0))
        return False
        
