# Problem: D - Great Photographer - https://codeforces.com/gym/590201/problem/D

n , x = list(map(int,input().split()))
left, right  = 0, 1000
for _ in range(n):
    a,b = list(map(int,input().split()))
    a,b = min(a,b), max(a,b)
    left,right = max(left,a),min(right,b)
if left > right:
    print(-1)
elif x <= left:
    print(left-x)
elif x>=right:
    print(x-right)
else:
    print(0)