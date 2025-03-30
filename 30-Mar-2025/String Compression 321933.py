# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        j = 0  
        i = 0  

        while i < n:
            char = chars[i] 
            count = 0  

            while i < n and chars[i] == char:
                count += 1
                i += 1 
            
            chars[j] = char
            j += 1

            if count > 1:
                for c in str(count):  
                    chars[j] = c
                    j += 1

        return j 


            