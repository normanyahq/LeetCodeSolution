class Solution(object):
    def generateResult(self, s, dp, wordDict):
        result = []
        stack = [(len(dp) - 1, len(dp) - 2)]
        while stack:
            pos, j = stack.pop()
            while j>=0 and (not dp[j] or s[j:pos] not in wordDict):
                j -= 1
            if j < 0:
                continue
            elif j == 0:
                pos_list = [0, pos] + [i[0] for i in stack[::-1]]
                sentence = " ".join([s[pos_list[i]:pos_list[i+1]] for i in range(len(pos_list)-1)])
                result.append(sentence)
            else:
                stack.append((pos, j-1))
                stack.append((j, j-1))
        return result
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for word in wordDict:
            if s.startswith(word):
                dp[len(word)] = True
        for i in xrange(1, len(s) + 1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                
        return self.generateResult(s, dp, wordDict)
        
