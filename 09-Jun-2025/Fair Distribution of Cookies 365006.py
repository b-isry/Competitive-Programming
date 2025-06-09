# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cur = [0] * k
        min_unfairness = float('inf')

        def solve(i, zero):
            nonlocal min_unfairness
            if n-i < zero: return

            if i == n:
                max_cookies = max(cur)
                min_unfairness = min(min_unfairness, max_cookies)
                return
            for j in range(k):
                zero -= int(cur[j] == 0)
                cur[j] += cookies[i]
                solve(i + 1, zero)
                cur[j] -= cookies[i]
                zero += int(cur[j] == 0)
        
        solve(0, k)
        return min_unfairness