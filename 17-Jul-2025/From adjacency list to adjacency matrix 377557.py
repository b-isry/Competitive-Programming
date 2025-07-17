# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
adj_matrix = [[0]*n for _ in range(n)]

for i in range(n):
    parts = list(map(int, input().split()))
    k = parts[0]
    for neighbor in parts[1:]:
        adj_matrix[i][neighbor - 1] = 1

for row in adj_matrix:
    print(*row)
