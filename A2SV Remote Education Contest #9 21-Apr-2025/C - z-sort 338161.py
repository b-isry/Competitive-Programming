# Problem: C - z-sort - https://codeforces.com/gym/603156/problem/C

n = int(input())
arr = list(map(int, input().split()))

i =  1

valid = True
while i < n:
    if (i + 1) % 2 == 0:
        if arr[i] < arr[i - 1]:
            if i > 1:
                if arr[i] > arr[i - 2]:
                    valid = False
                    break
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    else:
        if arr[i] > arr[i - 1]:
            if arr[i] < arr[i - 2]:
                valid = False
                break
            arr[i], arr[i - 1] = arr[i - 1], arr[i] 
    i += 1
    
if valid:
    print(*arr)
else:
    print("Impossible")    