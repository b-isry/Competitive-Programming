# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = defaultdict(int)
        for i in arr:
            pair = k - (i % k)
            if pair % k == 0 and c[0] > 0: c[0] -= 1
            elif c[pair] > 0: c[pair] -= 1
            else: c[i%k] += 1
        ans = True
        for _, i in c.items():
            if i > 0: ans = False
        return ans

        