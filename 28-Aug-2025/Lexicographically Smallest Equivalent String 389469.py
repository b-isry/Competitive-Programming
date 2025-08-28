# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        par = [i for i in range(26)]
        ans = []
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return
            if p1 < p2:
                par[p2] = p1
            else:
                par[p1] = p2
        
        for i in range(len(s1)):
            x, y = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            union(x, y)
        
        for ch in baseStr:
            root = find(ord(ch) - ord("a"))
            ans.append(chr(root + ord("a")))
        
        return "".join(ans)

