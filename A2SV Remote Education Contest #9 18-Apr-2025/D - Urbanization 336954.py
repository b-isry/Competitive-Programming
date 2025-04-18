# Problem: D - Urbanization - https://codeforces.com/gym/603156/problem/D

def urban(n, n1, n2, p):
    p.sort(reverse = True)
    
    if n1 > n2:
        n1, n2 = n2, n1
    
    top = p[:n1 + n2]
    
    c1 = top[:n1]
    c2 = top[n1:]
    
    res = float()
    res = sum(c1) / n1 + sum(c2) / n2
    print(f"{res:.8f}")
    
n, n1, n2 = map(int, input().split())
p = list(map(int, input().split()))
urban(n, n1, n2, p)