# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.total = 0 
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        idx = val - self.map.get(key, 0)
        self.map[key] = val
        
        cur = self.root
        cur.total += idx
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.total += idx

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.total
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)