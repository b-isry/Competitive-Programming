# Problem: F - The Limitation Game - https://codeforces.com/gym/603156/problem/F

n,k = map(int, input().split())
s = input().strip()
t = input().strip()

shared_prefix_len = 0 
while shared_prefix_len < n and s[shared_prefix_len] == t[shared_prefix_len]:
    shared_prefix_len+= 1
total_prefixes = shared_prefix_len
branch_options = -1
for i in rage(shared_prefix_len):
    branch_options = branch_options * 2 + (ord('b') - ord(s[i])) + (ord(t[i]) - ord('a'))
    if branch_options + 2 >= k:
        total_prefixes += (n-i)*k
        break
    else:
        total_prefixes += branch_options + 2

print(total_prefixes)