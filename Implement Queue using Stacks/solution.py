class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.stack2:
            self.stack2 = self.stack1
            self.stack2.reverse()
            self.stack1 = []
        self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack2:
            self.stack2 = self.stack1
            self.stack2.reverse()
            self.stack1 = []
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2
