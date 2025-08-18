# Problem: A - Maxim vs. Yogurt: The Great Discount Battle - https://codeforces.com/gym/629689/problem/A

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    total = 0

    if 2 * a > b:  
        total += (n // 2) * b
        if n % 2:  
            total += a
    else: 
        total += n * a

    print(total)
    