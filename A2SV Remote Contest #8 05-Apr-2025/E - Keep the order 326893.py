# Problem: E - Keep the order - https://codeforces.com/gym/599884/problem/E

def troops(n,a,b):
    count = 0
    max_idx = -1
     
    t2 = {b[i]: i for i in range(n)}
    
    for j in a:
        idx = t2[j]
        
        if idx < max_idx:
            count += 1
        else:   
            max_idx = idx

    return count

n = int(input().strip())
a = input().strip().split()
b = input().strip().split()
print(troops(n,a,b))