# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def helper(l, r):
            if l == r:
                return l
            pick = (l+r) // 2
            if guess(pick) == 1:
                return helper(pick+1, r)
            elif guess(pick) == -1:
                return helper(l, pick)
            else:
                return pick
        return helper(1, n)
        