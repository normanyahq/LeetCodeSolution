class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        answer = [[1]]
        for i in range (1, numRows):
            t = [1]
            for j in range(0, i-1):
                t.append(sum(answer[-1][j:j+2]))
            t.append(1)
            answer.append(t)
        return answer
