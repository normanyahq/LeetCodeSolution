class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        new_str = "\\n".join([i.replace('\\', '\\\\') for i in strs])
        if len(strs):
            new_str += '\\n'
        return new_str


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        s = s.split('\\n')
        return [s[i].replace('\\\\', '\\') for i in xrange(len(s)-1)]

