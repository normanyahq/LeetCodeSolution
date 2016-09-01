from collections import defaultdict
class Solution(object):

    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if not rectangles:
            return True
        rectangles.sort()
        min_x = rectangles[0][0]
        min_y = rectangles[0][1]
        max_x = rectangles[0][2]
        max_y = rectangles[0][3]
        area_count = 0
        for i in xrange(len(rectangles)):
            min_y = min(min_y, rectangles[i][1])
            max_x = max(max_x, rectangles[i][2])
            max_y = max(max_y, rectangles[i][3])
            area_count += (rectangles[i][2] - rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1])
        if area_count != (max_x - min_x) * (max_y - min_y):
            return False

        # use lower 4 bits to store the four corner types for each point
        corner_count = defaultdict(int)
        for i in xrange(len(rectangles)):
            x1, y1, x2, y2 = rectangles[i][:]
            corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for shift, corner in enumerate(corners):
                if (corner_count[corner] >> shift) & 1:
                    return False
                corner_count[corner] |= (1 << shift)

        # each point must have even number of corner types, except for 
        # the four corners of the whole area. Draw an example will help
        # you understand
        for corner in corner_count:
            if corner in [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]:
                continue
            if bin(corner_count[corner]).count("1") % 2:
                return False
        return True

