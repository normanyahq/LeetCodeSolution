import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        q_list = []
        envelopes = list(set([tuple(i) for i in envelopes]))
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        result = 0
        for w, h in envelopes:
            m = bisect.bisect_left(q_list, h)
            if m == len(q_list):
                q_list.append(h)
            else:
                q_list[m] = h
        return len(q_list)
