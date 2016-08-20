class Node:
    def __init__(self, _prev, _next, _key, _val):
        self.prev = _prev
        self.next = _next
        self.key = _key
        self.val = _val


class LRUDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.last = None

    def insert(self, node):
        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node
        if not self.last:
            self.last = self.head
        if self.capacity > self.size:
            self.size += 1
            return
        else:
            ret_value = self.last.key
            self.last = self.last.prev
            self.last.next = None
            return ret_value # used to remove hash

    def access(self, node):
        if node is self.head:
            return
        node.prev.next = node.next
        if node is self.last:
            self.last = node.prev
        else:
            node.next.prev = node.prev
        node.next = self.head
        self.head.prev = node
        node.prev = None
        self.head = node


class LRUCache():

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dequeue = LRUDeque(capacity)
        self.hashtable = dict()


    def get(self, key):
        """
        :rtype: int
        """
        if key in self.hashtable:
            self.dequeue.access(self.hashtable[key])
            return self.hashtable[key].val
        else:
            return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hashtable:
            self.dequeue.access(self.hashtable[key])
            self.hashtable[key].val = value
        else:
            self.hashtable[key] = Node(None, None, key, value)
            to_remove = self.dequeue.insert(self.hashtable[key])
            if to_remove:
                del self.hashtable[to_remove]

