# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        n = len(target)

        @lru_cache(None)
        def dfs(i: int) -> int:
            if i == n:
                return 0  

            node = root
            best = float('inf')

            for j in range(i, n):
                ch = target[j]
                if ch not in node.children:
                    break
                node = node.children[ch]
                best = min(best, 1 + dfs(j + 1))

            return best

        ans = dfs(0)
        return ans if ans != float('inf') else -1
