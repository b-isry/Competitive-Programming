# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            node = root
            for ch in word:
                node = node.children[ch]
            node.is_end = True

        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            node = root
            for j in range(i, len(s)):
                ch = s[j]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_end:
                    if dfs(j + 1):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)
