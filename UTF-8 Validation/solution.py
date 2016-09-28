class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        left = 0
        while left < len(data):
            if data[left] >> 7:
                leading_one = 1
                while leading_one <= 4 and (data[left] >> (7 - leading_one) & 1):
                    leading_one += 1
                if leading_one > 4 or leading_one < 2:
                    return False
                right = left + 1
                while right - left < leading_one:
                    if right >= len(data) or ((data[right] >> 6) & 11) != 2:
                        return False
                    right += 1
                left = right
            else:
                left += 1
        return True
