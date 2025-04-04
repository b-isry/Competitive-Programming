# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

def max_cards(cards, n):
    sereja = 0
    dima = 0
    left = 0
    right = n - 1
    
    for i in range(n):
        if cards[left] > cards[right]:
            if i % 2 == 0:
                sereja += cards[left]
            else:
                dima += cards[left]
            left += 1
        else:
            if i % 2 == 0:
                sereja += cards[right]
            else:
                dima += cards[right]
            right -= 1
    
  
    return  str(sereja) + " " + str(dima)

n = int(input().strip())
cards = list(map(int, input().strip().split()))
print(max_cards(cards, n))