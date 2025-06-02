# Problem: A - Can I Square? - https://codeforces.com/gym/609279/problem/A

import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)

    l, r = 0, total
    is_sq = False

    while l <= r:
        mid = (l + r) // 2
        square = mid * mid

        if square == total:
            is_sq = True
            break
        elif square < total:
            l = mid + 1
        else:
            r = mid - 1

    if is_sq:
        print("YES")
    else:
        print("NO")
