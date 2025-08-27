# Problem: A - Xorion and the Peaks - https://codeforces.com/gym/630556/problem/A

test = int(input())
for _ in range(test):
    n, k = map(int, input().split())
    
    if 2 * k >= n:
        print(-1)
        continue
    
    ans = []
    left = 1          
    right = n         
    
    for i in range(k):
        ans.append(left)
        ans.append(right)
        left += 1
        right -= 1
    
    for num in range(left, right + 1):
        ans.append(num)
    
    print(*ans)