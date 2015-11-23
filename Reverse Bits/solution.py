class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        binary = "0" * (32-len(binary)) + binary
        binary = (binary)
        answer = 0
        for i in range(0, len(binary)):
            answer += (1<<i) if binary[i] == '1' else 0
        return answer
