# Problem: D - Square Root Shuffle - https://codeforces.com/gym/608569/problem/D

def solve():
    """
    n (a + b) / 2 = sum
    """
    n = ini()
    double = n*2
    square = double**2
    s = (square * 2) / n
    half = s / 2
    sol = []
    sol.append(half - n)
    sol.append(half + n)
    for i in range(((n - 2) // 2)):
        sol.append(half - (i + 1))
        sol.append(half + (i + 1))

    if n % 2 == 1:
        sol.append(half)
        
    print(' '.join([str(int(val)) for val in sol]))