# Problem: C - Call for Robin - https://codeforces.com/gym/613405/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    if n <= 2:
        print(-1)
        continue
    
    left, right = 0, 10 * sum(arr)
    total = sum(arr)
    
    while left < right:
        mid = (left + right) // 2
        average_half = (total + mid) / (2 * n)
        
        if arr[n // 2] < average_half:
            right = mid
        else:
            left = mid + 1
    
    print(left)
