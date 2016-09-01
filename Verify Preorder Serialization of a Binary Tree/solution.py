class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        stack = [preorder[0]]
        i = 1
        while i < len(preorder) and stack and stack[0] != "#":
            c = preorder[i]
            if c == "#":
                stack.append("#")
                while stack[0] != '#' and stack[-1] == stack[-2] and stack[-1] == "#":
                    try:
                        stack.pop()
                        stack.pop()
                        stack.pop()
                    except:
                        return False
                    stack.append("#")

            else:
                stack.append(c)
            i += 1
        return i == len(preorder) and stack[0] == "#"
            

                
