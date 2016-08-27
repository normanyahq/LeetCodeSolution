import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.exists = dict()
        self.pool = list()
        self.size = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag = False
        self.pool.append(val)
        if val not in self.exists or not len(self.exists[val]):
            self.exists[val] = set([self.size])
            flag = True
        else:
            self.exists[val].add(self.size)
        self.size += 1
        return flag

        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.exists and len(self.exists[val]):
            index = self.exists[val].pop()
            self.exists[self.pool[-1]].add(index)
            self.exists[self.pool[-1]].remove(self.size-1)
            self.pool[index], self.pool[-1] = self.pool[-1], self.pool[index]
            self.pool.pop()
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.pool[random.randint(0, self.size-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
