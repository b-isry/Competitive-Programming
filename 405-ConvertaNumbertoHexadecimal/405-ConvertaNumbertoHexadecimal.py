# Last updated: 9/1/2026, 11:01:06 PM
1class Solution:
2    def toHex(self, num: int) -> str:
3        if num == 0:
4            return "0"
5
6        hex_chars = "0123456789abcdef"
7
8        num &= 0xFFFFFFFF
9
10        result = ""
11
12        while num > 0:
13            digit = num & 15
14            result = hex_chars[digit] + result
15            num >>= 4
16
17        return result