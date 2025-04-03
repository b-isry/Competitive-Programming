# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

def too_long(word):
    ab = []
    if len(word) > 10:
        ab.append(word[0])
        ab.append(str(len(word) - 2))   
        ab.append(word[-1])
        return ''.join(ab)
    else:
        return word

n = int(input().strip())
words = [input().strip() for _ in range(n)]
for word in words:
    print(too_long(word))