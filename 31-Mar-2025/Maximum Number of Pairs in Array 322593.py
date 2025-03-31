# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        lftovr = 0
        pair_map = {}

        for num in nums:
            if num in pair_map:
                pair_map[num] += 1
            else:
                pair_map[num] = 1
        
        for num, cnt in pair_map.items():
            pairs += cnt // 2
            lftovr += cnt % 2

        return [pairs, lftovr]

        