from collections import deque
class Solution(object):
    def bsearch(self, image, r1, r2, leftmost):
        left = r1
        right = r2
        while left <= right:
            mid = (left + right) / 2
            if any(i for i in image[mid] if i == '1'):
                if leftmost:
                    if mid > left and any(i for i in image[mid - 1] if i == '1'):
                        right = mid - 1
                    else:
                        return mid
                else:
                    if mid < right and any(i for i in image[mid + 1] if i == '1'):
                        left = mid + 1
                    else:
                        return mid
            else:
                if leftmost:
                    left = mid + 1
                else:
                    right = mid - 1
        return left

    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        max_x, min_x, max_y, min_y = x, x, y, y
        row = len(image)
        if row:
            col = len(image[0])
        min_x = self.bsearch(image, 0, x, True)
        max_x = self.bsearch(image, x, row-1, False)
        transposed_image = zip(*image)
        min_y = self.bsearch(transposed_image, 0, y, True)
        max_y = self.bsearch(transposed_image, y, col-1, False)
        return (max_x - min_x + 1) * (max_y - min_y + 1)

