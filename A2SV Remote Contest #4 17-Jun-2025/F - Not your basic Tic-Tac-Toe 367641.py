# Problem: F - Not your basic Tic-Tac-Toe - https://codeforces.com/gym/590201/problem/F

grid = []
#taking input
for i in range(11):
    #removing the space inbetween
    line = ''.join(input().split())

    #ignoring empty lines
    if line == "":
        continue

    grid.append(list(line))


x,y  = map(int,input().split())

#calculating the start of the box of the next move using the last input
startr = (((x-1)%3))*3
startc = (((y-1)%3))*3

#iterating through the valid cells inside the box and modifiying if they're available
flag = False
for i in range(startr,startr+3):
    for j in range(startc,startc+3):
        if grid[i][j] =='.':
            flag = True
            grid[i][j] = '!'

# if there were no available cell in the box then we can move anywhere so mark all available spots
if not flag:
    for i in range(9):
        for j in range(9):
            if grid[i][j] == '.':
                grid[i][j] ='!'

# since we removed all the empty spaces that are also required in the final output
# we need to reinsert them in final output 
ans = []
for i in range(11):
    if i == 3 or i == 7:
        ans.append('')
    else:
        curr = []
        for j in range(11):
            if j == 3 or j == 7:
                curr.append(' ')
            else:
                curr.append(grid[i-(i//4)][j-(j//4)])
        ans.append(curr)

#output the answer
for line in ans:
    print(''.join(line))
