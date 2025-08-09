# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]
        for i in range(1,rowIndex+1):
            row = [1]
            for j in range(1,i):
                row.append(ans[i-1][j-1] + ans[i-1][j])
            row.append(1)
            ans.append(row) 
        return ans[-1]
