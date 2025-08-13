# Problem: B - Planning Journey - https://codeforces.com/gym/625306/problem/B

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    hikes = 0
    length = 0

    for day in a:
        if day == 0:
            length += 1
        else:
            hikes += (length + 1) // (k + 1)
            length = 0

    hikes += (length + 1) // (k + 1)

    print(hikes)