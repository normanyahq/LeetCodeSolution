# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list_pointer = 0
        self.pointer_stack = []
        self.nested_list = nestedList

    def getValue(self, stack):
        v = self.nested_list[self.list_pointer]
        for i in xrange(len(stack)):
            v = v.getList()[stack[i]]
        return v
        
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            v = self.getValue(self.pointer_stack).getInteger()
            if len(self.pointer_stack):
                self.pointer_stack[-1] += 1
            else:
                self.list_pointer += 1
            return v
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.list_pointer < len(self.nested_list):
            if not len(self.pointer_stack):
                if self.getValue(self.pointer_stack).isInteger():
                    return True
                else:
                    self.pointer_stack.append(0)
            while len(self.pointer_stack):
                if self.pointer_stack[-1] == len(self.getValue(self.pointer_stack[:-1]).getList()):
                    self.pointer_stack.pop()
                    if self.pointer_stack:
                        self.pointer_stack[-1] += 1
                else:
                    if self.getValue(self.pointer_stack).isInteger():
                        return True
                    else:
                        self.pointer_stack.append(0)

            self.list_pointer += 1
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
