class Solution(object):
    def dfs(self, num_str, depth, stack, result):
        mapping = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        if depth == len(num_str):
            result.append("".join(stack))
            return
        for c in mapping[int(num_str[depth])]:
            stack.append(c)
            self.dfs(num_str, depth+1, stack, result)
            stack.pop()
        
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result = list()
        self.dfs(digits, 0, [], result)
        return result
        
