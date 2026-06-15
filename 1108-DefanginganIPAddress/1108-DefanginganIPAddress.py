# Last updated: 6/15/2026, 7:49:55 PM
1class Solution:
2    def defangIPaddr(self, address: str) -> str:
3        return address.replace(".", "[.]")