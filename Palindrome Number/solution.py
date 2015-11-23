class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Do this without extra space. <==> O(1) space


        if x < 10:
            return x >= 0
        digit_count = 0
        num = x
        while num:
            digit_count += 1
            num /= 10
        for i in range(0, digit_count/2):
            if x % 10 != x / (10**(digit_count-1-i * 2)):
                return False
            x %= (10**(digit_count-1-2*i))
            x /= 10
        return True
