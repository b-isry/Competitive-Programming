# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B

import sys

def solve():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    # Find the first and last occurrence of 'B'
    l = s.find('B')
    r = s.rfind('B')

    # Output the minimal segment length
    print(r - l + 1)

# Read number of test cases
t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve()