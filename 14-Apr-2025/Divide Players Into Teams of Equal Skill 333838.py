# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        res = 0

        right, left = n-1, 0
        total_skill = skill[left] + skill[right]
        while left < right:
            if total_skill != skill[left] + skill[right]:
                return -1
            else:
                res += skill[left] * skill[right]
 
            left += 1
            right -= 1
            
        return res
            
        

