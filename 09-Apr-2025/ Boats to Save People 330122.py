# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        boat = 0
        i, j = 0, n-1

        while i <= j:
            if people[i] + people[j] <= limit: 
                i += 1  
            j -= 1  
            boat += 1

        return boat
        