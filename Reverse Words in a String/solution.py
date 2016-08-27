class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        s = s.strip()
        new_s = []

        while i < len(s):
            if not i or s[i-1] !=' ' and s[i] == ' ' or s[i] != ' ':
                new_s.append(s[i])
            i += 1
        s = list(reversed(new_s))
        i, j = 0, 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[j] != ' ':
                j += 1
            k = j-1
            while i < k:
                s[i], s[k] = s[k], s[i]
                i += 1
                k -= 1
            i = j + 1
        return "".join(s).strip()
