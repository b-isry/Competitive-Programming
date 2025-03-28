# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = -1 

        for i, num in enumerate(nums):
            prefix_sum += num 
            remainder = prefix_sum % k

            if remainder not in prefix_sums:
                prefix_sums[remainder] = i

            elif i - prefix_sums[remainder] > 1: 
                    return True
        return False
       