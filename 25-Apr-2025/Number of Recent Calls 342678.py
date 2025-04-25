# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.cnt = deque()
        
    def ping(self, t: int) -> int:
        self.cnt.append(t)
        x = t - 3000
        while self.cnt and self.cnt[0] < x:
            self.cnt.popleft()
        return len(self.cnt)




        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)