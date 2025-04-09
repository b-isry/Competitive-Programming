# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        prefix_sums = [0]*(n+1)
        
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        for i in range(n):
            if (i-k) < 0 or (i+k) >= n:
                res.append(-1)
            else:
                total = prefix_sums[i+k+1] - prefix_sums[i-k]
                avg = total / ((i+k+1) - (i-k))
                res.append(floor(avg))
        return res