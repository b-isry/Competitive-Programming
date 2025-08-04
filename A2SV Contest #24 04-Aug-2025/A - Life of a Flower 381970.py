# Problem: A - Life of a Flower - https://codeforces.com/gym/626626/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    die = False
    tall = 1
    
    for i in range(n):
        if i == 0:
            if a[i] == 1:
                tall += 1
        else: 
            if a[i] == 0:
                if a[i-1] == 0:
                    die = True
                else: pass
            
            if a[i] == 1:
                if a[i-1] == 1:
                    tall += 5
                else:
                    tall += 1
    if not die:
        print(tall)
    else:  
        print(-1)
    