from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = deque()  
        self.hashMap = {}  

    def get(self, key: int) -> int:
        if key in self.hashMap:
            # Move the key to the most recently used position
            self.cache.remove(key)
            self.cache.append(key)
            return self.hashMap[key][1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key][1] = value
            self.cache.remove(key)
            self.cache.append(key)

        else:
            if len(self.cache) == self.capacity:
                oldest_key = self.cache.popleft()
                del self.hashMap[oldest_key]

            self.cache.append(key)
            self.hashMap[key] = [key, value]


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self,node):
        # node.prev = self.left
        # node.next = self.left.next
        # self.left.next.prev = node
        # self.left.next = node
        
        node.next = self.right
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(self.left.next)
            del self.cache[lru.key]
 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)