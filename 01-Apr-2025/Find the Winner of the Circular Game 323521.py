# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))
        start = 0

        while len(arr) > 1:
            rem = (start + k-1) % len(arr)
            arr.pop(rem)
            start = rem
        return arr[0]
