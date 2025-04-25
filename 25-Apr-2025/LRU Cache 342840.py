# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.capacity = capacity
        self.dummy_right = Node(None, None)
        self.dummy_left = Node(None, None)
        self.dummy_right.prev = self.dummy_left
        self.dummy_left.next = self.dummy_right

    def mover(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.dummy_left.next
        node.prev = self.dummy_left
        node.next.prev = node
        self.dummy_left.next = node
    
    def creater(self, key, value):
        node = Node(key, value)
        node.next = self.dummy_left.next
        node.prev = self.dummy_left
        node.next.prev = node
        self.dummy_left.next = node
        self.cache_dict[key] = node

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            self.mover(self.cache_dict[key])
            return self.cache_dict[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.mover(self.cache_dict[key])
            self.cache_dict[key].val = value
        else:
            if len(self.cache_dict) >= self.capacity:
                del self.cache_dict[self.dummy_right.prev.key]
                self.dummy_right.prev.prev.next = self.dummy_right
                self.dummy_right.prev = self.dummy_right.prev.prev
            self.creater(key, value)


            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)