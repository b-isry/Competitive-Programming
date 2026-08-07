# Last updated: 8/7/2026, 10:11:05 PM
1class Solution:
2    def smallestNumber(self, num: str, t: int) -> str:
3        temp = t
4        cnt = [0, 0, 0, 0]
5        for i, p in enumerate([2, 3, 5, 7]):
6            while temp % p == 0:
7                cnt[i] += 1
8                temp //= p
9                
10        if temp > 1:
11            return "-1"
12            
13        divs = []
14        for a in range(cnt[0] + 1):
15            for b in range(cnt[1] + 1):
16                for c in range(cnt[2] + 1):
17                    for d in range(cnt[3] + 1):
18                        divs.append((2**a) * (3**b) * (5**c) * (7**d))
19        divs.sort()
20        
21        trans = {v: [v] * 10 for v in divs}
22        for v in divs:
23            for d in range(1, 10):
24                trans[v][d] = v // math.gcd(v, d)
25                
26        dp = {v: float('inf') for v in divs}
27        dp[1] = 0
28        
29        for v in divs:
30            if v == 1:
31                continue
32            best = float('inf')
33            for d in range(2, 10):
34                nxt = trans[v][d]
35                if dp[nxt] + 1 < best:
36                    best = dp[nxt] + 1
37            dp[v] = best
38            
39        n = len(num)
40        first_zero = num.find('0')
41        
42        if first_zero == -1:
43            max_i_allowed = n - 1
44        else:
45            max_i_allowed = first_zero
46            
47        prefix_t = [t]
48        for i in range(max_i_allowed):
49            prefix_t.append(trans[prefix_t[-1]][int(num[i])])
50            
51        if first_zero == -1:
52            full_t = trans[prefix_t[-1]][int(num[-1])]
53            if full_t == 1:
54                return num
55                
56        for i in range(max_i_allowed, -1, -1):
57            p_t = prefix_t[i]
58            rem = n - 1 - i
59            
60            for d in range(int(num[i]) + 1, 10):
61                t_req = trans[p_t][d]
62                if dp[t_req] <= rem:
63                    ans = [num[:i], str(d)]
64                    curr_t = t_req
65                    for step in range(rem):
66                        for nxt_d in range(1, 10):
67                            next_t = trans[curr_t][nxt_d]
68                            if dp[next_t] <= rem - 1 - step:
69                                ans.append(str(nxt_d))
70                                curr_t = next_t
71                                break
72                    return "".join(ans)
73                    
74        length = max(n + 1, dp[t])
75        ans = []
76        curr_t = t
77        for step in range(length):
78            for nxt_d in range(1, 10):
79                next_t = trans[curr_t][nxt_d]
80                if dp[next_t] <= length - 1 - step:
81                    ans.append(str(nxt_d))
82                    curr_t = next_t
83                    break
84        return "".join(ans)