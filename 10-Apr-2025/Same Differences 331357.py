# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict
def equals(n, arr):
    diff_count = defaultdict(int)
    cnt = 0
    for i, val in enumerate(arr):
        key = val - i
        cnt += diff_count[key]
        diff_count[key] += 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(equals(n, arr))