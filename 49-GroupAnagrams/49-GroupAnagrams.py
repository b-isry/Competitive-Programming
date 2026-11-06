# Last updated: 11/6/2026, 3:09:16 AM
1class Solution:
2    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
3        res = defaultdict(list)
4        for str in strs:
5            k = "".join(sorted(str))
6            res[k].append(str)
7        return list(res.values())
8