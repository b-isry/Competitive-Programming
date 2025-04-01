# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = Counter(nums)
        majority = set()
        for num in nums:
            if x[num] > n/3:
                majority.add(num)

        return list(majority)
