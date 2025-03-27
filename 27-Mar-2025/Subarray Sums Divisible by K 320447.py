# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1 

        for num in nums:
            prefix_sum += num 
            remainder = prefix_sum % k

            count += prefix_sums[remainder]
            prefix_sums[remainder] += 1

        print(prefix_sums)
        return count