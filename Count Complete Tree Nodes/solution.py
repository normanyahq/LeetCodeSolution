# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, root):
        height = 0
        t = root
        while t:
            t = t.left
            height += 1
        return height
        
    def nodeExists(self, root, height, nodeCode):
        t = root
        for i in range(height-2, -1, -1):
            if (nodeCode >> i) & 1:
                t = t.right
            else:
                t = t.left
        return True if t else False
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height = self.getHeight(root)
        left = 0
        mid = 0
        right = (1<<(height-1))-1
        if self.nodeExists(root, height, right):
            return (2**height)-1
        while self.nodeExists(root, height, left):
            mid = (left + right) / 2
            if self.nodeExists(root, height, mid):
                left = mid + 1
            else:
                right = mid - 1
        return 2**(height-1) + mid 
            
        
        

                
        
        
