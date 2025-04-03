# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        num_map = Counter()
        cnt, j = 0, 0 
        n = len(nums)
        
        for i in range(n):
            k -= num_map[nums[i]]
            num_map[nums[i]] += 1

            while k <= 0:
                num_map[nums[j]] -= 1
                k += num_map[nums[j]]
                j += 1
            cnt += j
        return cnt
        