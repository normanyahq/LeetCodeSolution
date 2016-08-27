# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])
        s_idx = 0
        e_idx = 0
        max_conflict = 0
        conflict_count = 0
        while e_idx < len(end_times):
            if s_idx < len(start_times) and start_times[s_idx] < end_times[e_idx]:
                s_idx += 1
                conflict_count += 1
            elif s_idx == len(start_times) or start_times[s_idx] > end_times[e_idx]:
                e_idx += 1
                conflict_count -= 1
            else:
                s_idx += 1
                e_idx += 1
            max_conflict = max(max_conflict, conflict_count)
        return max_conflict
            
