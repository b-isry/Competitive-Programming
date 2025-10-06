# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            pr = {n & mask for n in nums}
            cd = max_xor | (1 << i)
            if any((cd ^ p) in pr for p in pr):
                max_xor = cd
        return max_xor