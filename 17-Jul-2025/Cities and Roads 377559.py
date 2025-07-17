# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
roads = 0

for i in range(n):
    for j in range(n):
        if adj[i][j] == 1:
            if i < j:
                roads += 1
print(roads)



