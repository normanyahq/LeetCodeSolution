class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        max_x = max(map(lambda x: x[0], points))
        min_x = min(map(lambda x: x[0], points))
        s = max_x + min_x
        seen_points = set([tuple(p) for p in points])
        for p in points:
            if (s-p[0], p[1]) not in seen_points:
                return False
        return True
