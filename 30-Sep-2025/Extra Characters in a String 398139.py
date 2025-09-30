# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie()
        for word in dictionary:
            node = root
            for ch in word:
                node = node.children[ch]
            node.is_end = True

        n = len(s)

        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0

            res = 1 + dp(i + 1)

            node = root
            j = i
            while j < n and s[j] in node.children:
                node = node.children[s[j]]
                if node.is_end:
                    res = min(res, dp(j + 1))
                j += 1

            return res

        return dp(0)