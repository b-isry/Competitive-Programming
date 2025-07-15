# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        di = {
            1: [(0, -1), (0, 1)],      
            2: [(-1, 0), (1, 0)],     
            3: [(0, -1), (1, 0)],     
            4: [(0, 1), (1, 0)],      
            5: [(0, -1), (-1, 0)], 
            6: [(0, 1), (-1, 0)] 
        }

        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }

        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        destination = (len(grid) - 1, len(grid[0]) - 1)

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(row, col):
            if (row, col) == destination:
                return True
            
            visited[row][col] = True

            for r, c in di[grid[row][col]]:
                nr = row + r
                nc = col + c

                if inbound(nr, nc) and not visited[nr][nc]:
                    if (opposite[(r, c)] in di[grid[nr][nc]]):
                        if dfs(nr, nc):
                            return True
            return False
        return dfs(0, 0)
