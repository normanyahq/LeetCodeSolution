class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet += alphabet.upper()
        alphabet = set(alphabet)
        digits = set("1234567890")
        
        
        stack = list()
        result = ""
        left = 0
        while left < len(s):
            if s[left] in alphabet:
                result += s[left]
                left += 1
            elif s[left] in digits:
                right = left + 1
                while s[right] in digits:
                    right += 1
                num = int(s[left:right])
                count_bracket = 1
                left = right
                right = left + 1
                while count_bracket:
                    if s[right] == "]":
                        count_bracket -= 1
                    elif s[right] == "[":
                        count_bracket += 1
                    right += 1
                result += num * self.decodeString(s[left+1:right-1])
                left = right
        return result
                    
