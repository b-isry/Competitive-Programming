# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]

source = []
sink = []

for i in range(n):
    if all(adj[i][j] == 0 for j in range(n)):
        sink.append(i + 1)
    
    if all(adj[j][i] == 0 for j in range(n)):
        source.append(i + 1)

print(len(source), *source)
print(len(sink), *sink)
