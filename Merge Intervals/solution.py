# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = list()
        intervals = sorted([(i.start, i.end,) for i in intervals])
        i = 0
        while i < len(intervals):
            cur_begin = intervals[i][0]
            cur_end = intervals[i][1]
            j = i+1
            while j < len(intervals) and intervals[j][0] <= cur_end:
                if intervals[j][1] > cur_end:
                    cur_end = intervals[j][1]
                j += 1
            result.append([cur_begin, cur_end])
            i = j
        return result
            
        
