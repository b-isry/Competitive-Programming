# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        str_cnt = 0
        n = len(s)
        
        for right in range(n):
            count[s[right]] += 1    
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                str_cnt += n - right
                count[s[left]] -= 1
                left += 1
                
        return str_cnt