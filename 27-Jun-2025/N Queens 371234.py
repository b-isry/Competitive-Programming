# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        d1 = set()
        d2 = set()
        board = [['.']*n for _ in range(n)]

        def back(row):
            if row == n:
                ans = [''.join(row) for row in board]
                res.append(ans)
                return
            for col in range(n):
                if col in cols or (row-col) in d2 or (row+col) in d1:
                    continue
                
                cols.add(col)
                d2.add(row-col)
                d1.add(row+col)
                board[row][col] = 'Q'

                back(row+1)

                cols.remove(col)
                d2.remove(row-col)
                d1.remove(row+col)
                board[row][col] = '.'

        back(0)

        return res