# Problem: Team - https://codeforces.com/contest/231/problem/A

def team(a, n):
    cnt = 0
    for i in a:
        if sum(i) >= 2: 
            cnt += 1
    return cnt
    

n = int(input().strip()) 
a = [list(map(int, input().split())) for _ in range(n)]
print(team(a, n))