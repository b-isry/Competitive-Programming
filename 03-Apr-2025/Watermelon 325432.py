# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A


def watermelon(w):
    if w % 2 == 0 and  w > 2:
        return 'yes'
    return "no"
    
w = int(input())
print(watermelon(w))