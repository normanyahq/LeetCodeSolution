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
        
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_count = dict()
        stack = list([(root, 0)])
        result = 0
        while stack:
            node, state = stack.pop()
            if node:
                print node.val, state
            if not node: 
                continue
            if not node.left and not node.right:
                node_count[node.val] = 1
            if state == 0:
                stack.append((node, 1))
                if node.left:
                    stack.append((node.left, 0))
            elif state == 1:
                stack.append((node, 2))
                if node.right:
                    stack.append((node.right, 0))
            elif state == 2:
                node_count[node.val] = 1 + (node_count[node.left.val] if node.left else 0) + (node_count[node.right.val] if node.right else 0)
                if self.isValidBST(node) and result < node_count[node.val]:
                    result = node_count[node.val]
        return result
            
    

