# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    if x % 2 == 1:
        print(2) 
    elif (x & (x - 1)) == 0:  
        print(x + 1)
    else:
        print(x & -x) 
