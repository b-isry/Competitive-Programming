# Last updated: 11/23/2026, 9:25:31 PM
1class ProductOfNumbers:
2
3    def __init__(self):
4        self.prefix = [1]
5
6    def add(self, num: int) -> None:
7        if num == 0:
8            self.prefix = [1]
9        else:
10            self.prefix.append(self.prefix[-1] * num)
11
12    def getProduct(self, k: int) -> int:
13        if k >= len(self.prefix):
14            return 0
15
16        return self.prefix[-1] // self.prefix[-k - 1]
17
18
19# Your ProductOfNumbers object will be instantiated and called as such:
20# obj = ProductOfNumbers()
21# obj.add(num)
22# param_2 = obj.getProduct(k)