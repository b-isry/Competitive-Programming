# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colored = {} 
        freq = {} 
        ans = []
        for ball , clr in queries:
            if ball in colored:
                old_color = colored[ball]
                freq[old_color] -= 1
                if freq[old_color] == 0:
                    del freq[old_color]

            colored[ball] = clr
            freq[clr] = freq.get(clr , 0) + 1
            ans.append(len(freq))

        return ans