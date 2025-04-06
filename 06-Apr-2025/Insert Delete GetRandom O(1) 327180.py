# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.random_num = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.random_num:
            self.random_num.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.random_num:
            self.random_num.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(list(self.random_num))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()