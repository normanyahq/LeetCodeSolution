class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result_len1 =["0", "1", "8"]
        result_len2 = ["00", "11", "69", "88", "96"]
        result = []
        if n == 1:
            return result_len1
        elif n == 2:
            return result_len2[1:]
        elif n >= 3:
            result = result_len1 if n % 2 else result_len2
            n -= 1 if n % 2 else 2
            while n:
                new_result = []
                for nums in result_len2[n<=2:]:
                    for st in result:
                        new_result.append(nums[0] + st + nums[1])
                n -= 2
                result = new_result

        return result
