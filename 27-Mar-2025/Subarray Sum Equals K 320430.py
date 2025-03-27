# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  
        
        for num in nums:
            prefix_sum += num 
            
            if (prefix_sum - k) in prefix_sums:
                count += prefix_sums[prefix_sum - k]  
            prefix_sums[prefix_sum] += 1
              
        print(prefix_sums)
        return count