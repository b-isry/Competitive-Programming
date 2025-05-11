# Problem: A - Stairway to Goodness - https://codeforces.com/gym/608569/problem/A

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    low, high = 1, int(2e5)
    ans = 1
    while low <= high:
        mid = (low + high) // 2
        total = mid * (mid - 1) // 2
        if l + total <= r:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)