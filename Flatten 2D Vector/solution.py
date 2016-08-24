class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.arr = vec2d
        self.outer_pointer = 0
        self.inner_pointer = 0
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            v = self.arr[self.outer_pointer][self.inner_pointer]
            self.inner_pointer += 1
            return v
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.outer_pointer < len(self.arr):
            if self.inner_pointer < len(self.arr[self.outer_pointer]):
                return True
            else:
                self.inner_pointer = 0
                self.outer_pointer += 1
        return False
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
