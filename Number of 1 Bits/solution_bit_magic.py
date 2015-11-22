class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit_shift_array = [1, 2, 4, 8, 16]
        bit_and_high = [0xAAAAAAAA, 0xCCCCCCCC, 0xF0F0F0F0, 0xFF00FF00, 0xFFFF0000]
        bit_and_low = [0x55555555, 0x33333333, 0x0F0F0F0F, 0x00FF00FF, 0x0000FFFF]
        for shift, high, low in zip(bit_shift_array, bit_and_high, bit_and_low):
            n = (n & low) + ((n & high) >> shift)
            
        return n
