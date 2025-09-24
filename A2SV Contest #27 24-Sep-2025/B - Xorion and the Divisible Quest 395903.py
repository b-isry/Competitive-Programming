# Problem: B - Xorion and the Divisible Quest - https://codeforces.com/gym/630556/problem/B

n = int(input())
arr = list(map(int, input().split()))

# Find the minimum value in the array
min_value = float("inf")
for curr_num in arr:
    min_value = min(min_value, curr_num)
    
# Check if the minimum value divides all elements
is_valid = True
for curr_num in arr:
    if curr_num % min_value != 0:
        is_valid = False
        break

if is_valid:
    print(min_value)
else:
    print(-1)
