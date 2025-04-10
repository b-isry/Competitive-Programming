# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        my_coin = 0 
        n = len(piles) // 3

        for i in range(n):
            my_coin += piles[2 * i + 1]

        return my_coin