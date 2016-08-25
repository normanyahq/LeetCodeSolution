class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.lists = [v1, v2]
        self.pointer_list = [0] * 2
        self.cur_list = 0
        self.total_size = sum(len(i) for i in self.lists)
        self.got = 0
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            v = self.lists[self.cur_list][self.pointer_list[self.cur_list]]
            self.pointer_list[self.cur_list] += 1
            self.cur_list = (self.cur_list + 1) % len(self.lists)
            self.got += 1
            return v

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.got < self.total_size:
            if len(self.lists[self.cur_list]) > self.pointer_list[self.cur_list]:
                return True
            else:
                self.cur_list = (self.cur_list + 1) % len(self.lists)
        return False
                
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
