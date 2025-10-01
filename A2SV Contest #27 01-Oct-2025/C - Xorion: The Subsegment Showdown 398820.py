# Problem: C - Xorion: The Subsegment Showdown - https://codeforces.com/gym/630556/problem/C

def get_bits(n):
    
    bits = [0] * 32
    index = 31
    while n > 0:
        bits[index] = n % 2
        n //= 2
        index -= 1
    return bits

test = int(input())
for _ in range(test):
    x, y = map(int, input().split())
    count = 0
    #  Bits Repr of X and Y
    x_bits = get_bits(x)
    y_bits = get_bits(y)
    ans = 1
    
    for i in range(31, -1, -1):
        if x_bits[i] == y_bits[i]:
            ans *= 2
        else:
            break
    
    print(ans)