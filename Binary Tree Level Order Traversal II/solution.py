# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque()
        #define tuple (node, depth)
        queue.append((root, 1,))
        while len(queue):
            node, depth = queue.popleft()
            if len(result) < depth:
                result.insert(0, [])
            result[0].append(node.val)
            if node.left:
                queue.append((node.left, depth+1, ))
            if node.right:
                queue.append((node.right, depth+1, ))
        return result
