# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ans = -1

        queue = deque([(entrance[0], entrance[1], 0)])
        seen = set([(entrance[0], entrance[1])])
        di = [[1,0],[0,1],[-1,0],[0,-1]]

        rows, cols = len(maze), len(maze[0])

        while queue and ans == -1:
            row, col, step = queue.popleft()
            for i, j in di:
                x, y = row + j, col + i
                if 0 <= x < rows and 0 <=y < cols and maze[x][y] == '.' and (x,y) not in seen:
                    if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                        ans = step + 1
                    queue.append((x,y, step + 1))
                    seen.add((x,y))

        return ans   

