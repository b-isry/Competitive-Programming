# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = Counter()
        cnt = 0

        for i in answers:
            rabbits[i] += 1
        
        for x,y in zip(rabbits.keys(), rabbits.values()):
            cnt += ceil(y/(x+1))*(x+1)
        
        return cnt
        