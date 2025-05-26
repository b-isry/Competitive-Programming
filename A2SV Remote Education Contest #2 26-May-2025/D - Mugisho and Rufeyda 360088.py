# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

n , t = list(map(int,input().split()))

if t < 10:
    print(n * str(t))
else:
    if n==1:
        print(-1)
    else:
        print(10**(n-1))