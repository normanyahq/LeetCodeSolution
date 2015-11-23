# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path, solution, stack = [], [], []
        # define tuple in stack: (node, state)
        # state = 0: not visited
        # state = 1: visited left child
        # state = 2: visited right child
        if not root:
            return []
        stack.append((root, 0,))
        while stack:
            node, state = stack.pop()
            if state == 0:
                path.append(str(node.val))
                stack.append((node, 1,))
                if node.left:
                    stack.append((node.left, 0,))
            elif state == 1:
                stack.append((node, 2,))
                if node.right:
                    stack.append((node.right, 0,))
            elif state == 2:
                if not node.left and not node.right:
                    solution.append("->".join(path))
                path.pop()
        return solution
