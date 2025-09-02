# Problem: A - Loopix: Multiples Hunt - https://codeforces.com/gym/632067/problem/A

def solve(l, r, k):
    low, high = l, r
    x_max = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid * k <= r:
            x_max = mid       
            low = mid + 1     
        else:
            high = mid - 1    
    return max(x_max - l + 1, 0)



test = int(input())

for _ in range(test):
    l, r, k = map(int, input().split())
    print(solve(l, r, k))