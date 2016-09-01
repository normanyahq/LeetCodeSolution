import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap = list()
        self.max_heap = list()
        self.val = None

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.val == None:
            self.val = num
        else:
            if len(self.min_heap) < len(self.max_heap):
                if self.val <= num:
                    heapq.heappush(self.min_heap, num)
                else:
                    heapq.heappush(self.min_heap, self.val)
                    self.val = num
                    if self.max_heap:
                        c = -self.max_heap[0]
                        if c > self.val:
                            heapq.heappop(self.max_heap)
                            heapq.heappush(self.max_heap, -self.val)
                            self.val = c
            else:
                if self.val >= num:
                    heapq.heappush(self.max_heap, -num)
                else:
                    heapq.heappush(self.max_heap, -self.val)
                    self.val = num
                    if self.min_heap:
                        c = self.min_heap[0]
                        if c < self.val:
                            heapq.heappop(self.min_heap)
                            heapq.heappush(self.min_heap, self.val)
                            self.val = c


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return self.val / 1.
        elif len(self.min_heap) > len(self.max_heap):
            return (self.val + self.min_heap[0]) / 2.
        else:
            return (self.val - self.max_heap[0]) / 2.

