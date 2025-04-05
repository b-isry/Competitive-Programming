# Problem: A - Winners get Diabetes - https://codeforces.com/gym/599884/problem/A

def candy(n, a):
    count = {}
    candies = 0
    for i in range(n):
        if a[i] in count:
            count[a[i]] += 1
            candies += 1
        else:
            count[a[i]] = 2
            candies += 2
    return candies


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = input().strip() 
    print(candy(n, a))