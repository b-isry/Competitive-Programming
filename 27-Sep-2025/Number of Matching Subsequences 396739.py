# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.count = 0

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def dfs(node, idx):
            total = node.count

            for ch, child in node.children.items():
                next_id = s.find(ch, idx)
                if next_id != -1:
                    total += dfs(child, next_id + 1)
            return total

        root = Trie()
        for word in words:
            node = root
            for ch in word:
                node = node.children[ch]
            node.count += 1  
        return dfs(root, 0)