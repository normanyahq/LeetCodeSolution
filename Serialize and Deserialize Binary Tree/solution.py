from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        return str(root.val) + " " + self.serialize(root.left) + " " + self.serialize(root.right)

    def construct(self, values):
        v = values.popleft()
        if v == "#":
            return None
        p = TreeNode(int(v))
        p.left = self.construct(values)
        p.right = self.construct(values)
        return p
        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = deque(data.split())
        if not values:
            return None
        return self.construct(values)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
