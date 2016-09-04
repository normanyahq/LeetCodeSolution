# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache_val = None
        if self.iterator.hasNext():
            self.cache_val = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.cache_val != None:
            return self.cache_val
        

    def next(self):
        """
        :rtype: int
        """
        ret_val = self.cache_val
        if self.iterator.hasNext():
            self.cache_val = self.iterator.next()
        else:
            self.cache_val = None
        return ret_val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cache_val != None:
            return True
        else:
            return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
