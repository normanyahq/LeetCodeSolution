class Solution(object):
    state_result = dict() # False: lose state True: victory state
        
    def loseState(self, s):
        for i in range(len(s)-1):
            if s[i:i+2] == "++":
                return False
        return True
    
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in Solution.state_result:
            return Solution.state_result[s]
        
        if self.loseState(s):
            Solution.state_result[s] = False
            return False
        
        for i in range(len(s)-1):
            if s[i:i+2] == "++" and not self.canWin(s[:i] + "--" + s[i+2:]):
                Solution.state_result[s] = True
                return True
        Solution.state_result[s] = False
        return False
        

        
        
            
