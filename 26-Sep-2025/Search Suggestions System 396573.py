# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def suggest(self, prefix):
        def dfs(node, path, result):
            if node.is_end:
                result.append(path)
            for ch in sorted(node.children):
                child = node.children[ch]
                dfs(child, path + ch, result)
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        dfs(node, prefix, results)
        return results

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie() 
        
        for p in products:
            trie.insert(p)
        
        prefix = ""
        result = []

        for ch in searchWord:
            prefix += ch
            suggestions = trie.suggest(prefix)[:3] 
            result.append(suggestions)
        
        return result