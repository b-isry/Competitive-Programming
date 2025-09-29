# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        for word in words:
            node = root
            for ch in word:
                node = node.children[ch]
            node.is_end = True

        best_word = ""

        def dfs(node, path):
            nonlocal best_word
            if len(path) > len(best_word) or (len(path) == len(best_word) and path < best_word):
                best_word = path

            for char in sorted(node.children.keys()):
                child = node.children[char]
                if child.is_end:
                    dfs(child, path + char)

        dfs(root, "")
        return best_word
