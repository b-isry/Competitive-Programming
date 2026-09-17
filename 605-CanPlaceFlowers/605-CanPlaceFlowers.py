# Last updated: 9/17/2026, 10:13:21 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
3        if n == 0:
4            return True
5
6        for i in range(len(flowerbed)):
7            if flowerbed[i] == 0:
8                left = i == 0 or flowerbed[i - 1] == 0
9                right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
10
11                if left and right:
12                    flowerbed[i] = 1
13                    n -= 1
14
15                    if n == 0:
16                        return True
17
18        return False