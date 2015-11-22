class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        pos = len(digits) - 1
        digits[pos] += 1
        while pos and digits[pos] == 10:
            digits[pos] = 0
            digits[pos - 1] += 1
            pos -= 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits
