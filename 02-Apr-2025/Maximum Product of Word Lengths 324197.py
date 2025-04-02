# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        max_product = 0
        char_set = []
            
        for i in range(len(words)):
            char_set.append(set(words[i]))
                                                            
        for i in range(len(words)):

            for j in range(i+1,len(words)):
                if not (char_set[i] & char_set[j]):
                        
                    if max_product<(len(words[i])*len(words[j])):
                        max_product=len(words[i])*len(words[j])

        return max_product


                    
        