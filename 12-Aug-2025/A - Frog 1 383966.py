# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
h = list(map(int, input().split()))

memo = [0] * n
memo[0] = 0
memo[1] = abs(h[1] - h[0])

for i in range(2, n):
    memo[i] = min(memo[i-1] + abs(h[i] - h[i-1]), memo[i-2] + abs(h[i] - h[i-2]))

print(memo[n-1])