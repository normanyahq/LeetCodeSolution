# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer = []
        if not root:
            return answer
        from collections import deque
        q = deque()
        q.append((root, 1,))
        while q:
            node, depth = q.popleft()
            if depth > len(answer):
                answer.append([])
            answer[-1].append(node.val)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return answer
