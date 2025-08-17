# Problem: F - Tree Recoloring - https://codeforces.com/gym/628023/problem/F

import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

n, m = map(int, input().split())
colors = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# Euler Tour Flattening
tin = [0] * (n + 1)
tout = [0] * (n + 1)
order = [0] * (n + 1)
timer = 0

def dfs(u, p):
    global timer
    timer += 1
    tin[u] = timer
    order[timer] = u
    for v in adj[u]:
        if v != p:
            dfs(v, u)
    tout[u] = timer

dfs(1, -1)

size = 1
while size < n:
    size <<= 1

tree = [0] * (2 * size)
lazy = [-1] * (2 * size)

def build():
    for i in range(1, n + 1):
        node = order[i]
        tree[size + i - 1] = 1 << (colors[node - 1] - 1)
    for i in range(size - 1, 0, -1):
        tree[i] = tree[i * 2] | tree[i * 2 + 1]

def apply(node, value):
    tree[node] = value
    lazy[node] = value

def push(node):
    if lazy[node] != -1:
        apply(node * 2, lazy[node])
        apply(node * 2 + 1, lazy[node])
        lazy[node] = -1

def update(l, r, value, node=1, lx=1, rx=size):
    if r < lx or rx < l:
        return
    if l <= lx and rx <= r:
        apply(node, value)
        return
    push(node)
    mid = (lx + rx) // 2
    update(l, r, value, node * 2, lx, mid)
    update(l, r, value, node * 2 + 1, mid + 1, rx)
    tree[node] = tree[node * 2] | tree[node * 2 + 1]

def query(l, r, node=1, lx=1, rx=size):
    if r < lx or rx < l:
        return 0
    if l <= lx and rx <= r:
        return tree[node]
    push(node)
    mid = (lx + rx) // 2
    return query(l, r, node * 2, lx, mid) | query(l, r, node * 2 + 1, mid + 1, rx)

build()

for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        v, c = q[1], q[2]
        update(tin[v], tout[v], 1 << (c - 1))
    else:
        v = q[1]
        res = query(tin[v], tout[v])
        print(res.bit_count()) 