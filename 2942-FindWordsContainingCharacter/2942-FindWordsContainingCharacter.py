# Last updated: 8/24/2026, 10:41:46 PM
1class Solution:
2    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
3        result = []
4
5        for i in range(len(words)):
6            if x in words[i]:
7                result.append(i)
8
9        return result