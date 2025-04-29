# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

wire = input()
result = []

for val in wire:
    if not result:
        result.append(val)
        continue
    if result[-1] != val:
        result.append(val)
    else:
        while result and val == result[-1]:
            result.pop()

if result:
    print('No')
else:
    print('Yes')