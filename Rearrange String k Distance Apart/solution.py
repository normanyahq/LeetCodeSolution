from collections import defaultdict
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq_dict = defaultdict(int)
        bucket_pos = 0
        result = [''] * len(s)
        for c in s:
            freq_dict[c] += 1
        freq_list = sorted(freq_dict.items(), key=lambda x: -x[1])
        if not k:
            return s
        m = len(s) // k
        q = len(s) % k
        cur_pos = 0
        bucket_pos = 0
        for c, v in freq_list:
            if v == (m + (q>0)):
                q -= 1
            elif v > (m + (q>0)):
                return ""
            while v:
                result[cur_pos] = c
                cur_pos += k 
                if cur_pos >= len(s):
                    cur_pos = bucket_pos + 1
                    bucket_pos += 1
                v -= 1
            
        return "".join(result)
        

            
        
