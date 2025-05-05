# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        s =  2 ** n
        if k < s//2:
            return self.findKthBit(n-1, k)
        elif k == s//2:
            return "1"
        else:
            return "1" if self.findKthBit(n-1, s- k)== "0" else "0"



