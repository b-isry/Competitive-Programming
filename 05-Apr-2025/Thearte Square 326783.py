# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

def theatre(n, m, a):
    tiles = ((n + a - 1) // a) * ((m + a - 1) // a)
    return tiles

n, m, a = map(int, input().split())
print(theatre(n, m, a))