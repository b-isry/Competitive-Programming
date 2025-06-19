# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits: return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def back(idx, comb):
            if idx == len(digits):
                res.append(comb[:])
                return
            
            for i in digit_to_letters[digits[idx]]:
                back(idx + 1, comb+i)
        back(0, "")
        return res
