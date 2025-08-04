# Problem: B - Make Product Equal One - https://codeforces.com/gym/626626/problem/B

n = int(input())
a = list(map(int, input().split()))

cnt = 0
neg = 0
z = 0

for num in a:
    if num > 1:
        cnt += num - 1
    elif num < -1:
        cnt += -1 - num
        neg += 1
    elif num == 0:
        cnt += 1
        z += 1
    elif num == -1:
        neg += 1

if neg % 2 == 1:
    if z == 0:
        cnt += 2  

print(cnt)
