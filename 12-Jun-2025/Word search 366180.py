# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        di = [(0,1), (1,0), (0,-1), (-1,-0)]

        def backtrack(path, row, col, visited):
            if len(path) == len(word):
                return True

            for r,c in di:
                n_r = row + r
                n_c = col + c

                if bound(n_r,n_c) and board[n_r][n_c] == word[len(path)] and (n_r, n_c) not in visited:
                    path.append(board[n_r][n_c])
                    visited.add((n_r, n_c))

                    if backtrack(path, n_r, n_c, visited):
                        return True
                    path.pop()
                    visited.remove((n_r, n_c))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])): 
                path = []
                visited = set()

                if board[i][j] == word[len(path)]:
                    path.append(board[i][j])
                    visited.add((i, j))

                    if backtrack(path, i, j, visited):
                        return True
                    path.pop()
                    visited.remove((i, j))

        return False


