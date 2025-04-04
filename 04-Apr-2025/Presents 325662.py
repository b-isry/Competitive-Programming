# Problem: Presents - https://codeforces.com/problemset/problem/136/A

def present(gifts, n):
    res = [0] * n 
    for i in range(n):
        res[gifts[i]-1] =i + 1
    return res


n = int(input().strip())    
gifts = list(map(int, input().strip().split()))
result = present(gifts, n)
print(*result)