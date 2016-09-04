from collections import defaultdict
class Solution(object):
    def dfs(self, left, right, n, stack, result):
        if left == n and right == n:
            result.append("".join(stack))
        if left < n:
            stack.append("(")
            self.dfs(left+1, right, n, stack, result)
            stack.pop()
        if right < left:
            stack.append(")")
            self.dfs(left, right+1, n, stack, result)
            stack.pop()
        
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = list()
        self.dfs(0, 0, n, list(), result) 
        return result
