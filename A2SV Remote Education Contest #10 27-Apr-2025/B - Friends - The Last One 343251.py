# Problem: B - Friends - The Last One - https://codeforces.com/gym/604857/problem/B

t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = 0
    arr.sort(reverse=True)
    
    for i in range(n):
        if i == 0:
            res += arr[i] * 2 + 1
        elif i == n-1:
            res += 1
        else:
            res += arr[i] + 1  
    if res <= m:
        print("Yes")
    else:          
        print("No")