class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Parentheses = {u']':u'[', u'}':u'{', u')':u'('}
        stack = []
        for c in s:
            if c not in Parentheses:
                stack.append(c)
            else:
                if not stack or stack.pop() != Parentheses[c]:
                    return False
            
        return not stack
