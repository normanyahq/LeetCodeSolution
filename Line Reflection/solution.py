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
        avg = (max_x + min_x)
        points = sorted(list(set([(p[0], p[1],) for p in points if p[0] * 2 != avg])))
        if len(points) % 2:
            return False
        points = sorted(points[:len(points)/2], key=lambda x: (x[0], -x[1])) + sorted(points[len(points)/2:])
        left = 0
        right = len(points) - 1
        print points
        while left < right:
            if points[left][1] != points[right][1] or points[left][0] + points[right][0] != avg:
                return False
            left += 1
            right -= 1
        return True
