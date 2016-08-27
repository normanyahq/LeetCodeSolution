class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lines = input.split('\n')
        path = []
        cur_len = 0
        max_len = 0
        for line in lines:
            blank_count = - len(line.lstrip('\t')) + len(line)
            line = line.strip('\t')
            while blank_count < len(path):
                cur_len -= len(path.pop())
            if '.' in line:
                max_len = max(max_len, cur_len + len(path) + len(line))
            else:
                path.append(line)
                cur_len += len(line)
        return max_len
