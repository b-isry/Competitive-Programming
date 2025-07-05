# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        temp = defaultdict(lambda: -1)
        nr = len(mat)
        nc = len(mat[0])
        q = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0: q.append((i,j,-1))

        directions = [[1,0], [0,1], [-1,0],[0,-1]]
        while q:
            r, c, step = q.popleft()
            if temp[(r,c)] == -1: temp[(r,c)] =  step + 1
            for j, i in directions:
                dr, dc = r + j, c + i
                if 0 <= dr < nr and 0 <= dc < nc and mat[dr][dc] == 1:
                    mat[dr][dc] = 0
                    q.append((dr,dc,step + 1))

        ans = [[temp[(i,j)] for j in range(nc)] for i in range(nr)]
        return ans
