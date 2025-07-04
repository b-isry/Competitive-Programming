# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1: 
                    q.append((i,j,0))
                    visited.add((i,j))
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            r, c, step = q.popleft()
            isWater[r][c] = step
            for i,j in directions:
                dr,dc = r + i, c + j
                if 0 <= dr < len(isWater) and 0 <= dc < len(isWater[0]) and (dr,dc) not in visited:
                    visited.add((dr,dc))
                    q.append((dr,dc, step+1))
        return isWater