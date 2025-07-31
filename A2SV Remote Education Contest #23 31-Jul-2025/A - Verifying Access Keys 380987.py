# Problem: A - Verifying Access Keys - https://codeforces.com/gym/625306/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    key = input()

    last_digit = '0'
    last_letter = 'a'
    seen_letter = False
    is_secure = True

    for ch in key:
        if ch.isdigit():
            if seen_letter:
                is_secure = False
                break
            if ch < last_digit:
                is_secure = False
                break
            last_digit = ch
        else:
            if ch < last_letter:
                is_secure = False
                break
            last_letter = ch
            seen_letter = True

    print("YES" if is_secure else "NO")
