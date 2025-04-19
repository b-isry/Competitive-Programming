# Problem: B - Ski Resort - https://codeforces.com/gym/603156/problem/B

def cnt_days(n, k, q, temp):
    if n < k:
       print(0)
    cnt = 0
    valid = 0
    
    for i in range(n):
        if temp[i] <= q:
            valid += 1
            if valid >= k:
                cnt += valid - k + 1
        else:
            valid = 0
    return cnt


t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    temp = list(map(int, input().split()))
    print(cnt_days(n, k, q, temp))