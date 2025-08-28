# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par = [i for i in range(26)]
        rank = [1] * 26

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p2] += 1
            else:
                par[p1] = p2
                rank[p1] += 1
            return True
        
        for eq in equations:
            if eq[1:3] == "==":
                x, y = ord(eq[0]) - ord("a"), ord(eq[3]) - ord("a")
                union(x, y)

        for eq in equations:
            if eq[1:3] == "!=":
                x, y = ord(eq[0]) - ord("a"), ord(eq[3]) - ord("a")
                if find(x) == find(y):
                    return False

        return True
        
