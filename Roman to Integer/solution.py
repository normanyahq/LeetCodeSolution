class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        add = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000 }
        sub = {'IV': 2,
                'IX': 2,
                'XL': 20,
                'XC': 20,
                'CD': 200,
                'CM': 200 }
        answer = 0
        for c in s:
            answer += add[c]
        for k in sub:
            if k in s:
                answer -= sub[k]
        return answer

