from collections import deque

# a standard queue only allows: push(), pop()

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queues = [deque(), deque()]
        self.main = 0
        self.auxiliary = 1

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queues[self.main].append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.queues[self.main]) > 1:
            # (x & 1) ^ 1 <=> (x + 1) % 2
            self.queues[self.auxiliary].append(self.queues[self.main].popleft())
        return_value = self.queues[self.main].popleft()    
        
        while len(self.queues[self.auxiliary]):
            # (x & 1) ^ 1 <=> (x + 1) % 2
            self.queues[self.main].append(self.queues[self.auxiliary].popleft())
        return return_value

    def top(self):
        """
        :rtype: int
        """
        the_other_queue = (self.main & 1) ^ 1
        while len(self.queues[self.main]) > 1:
            # (x & 1) ^ 1 <=> (x + 1) % 2
            self.queues[self.auxiliary].append(self.queues[self.main].popleft())
        return_value = self.queues[self.main][0]   
        return return_value

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.queues[0]) and not len(self.queues[1])        
