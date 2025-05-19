# Problem: E - NATOLI's String Quest - https://codeforces.com/gym/605795/problem/E

s = input()
count = [0] * 26
for c in s:
    count[ord(c) - ord('a')] += 1

stack = []
answer = []

for c in s:
    idx = ord(c) - ord('a')
    stack.append(c)
    count[idx] -= 1

    while stack:
        top = stack[-1]
        top_idx = ord(top) - ord('a')

        if any(count[i] > 0 for i in range(top_idx)):
            break
        answer.append(stack.pop())

print(''.join(answer))