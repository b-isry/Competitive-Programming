# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False
        self.words = set()

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        root = Trie()
        
        for i, word in enumerate(arr):       
            for start in range(len(word)):   

                node = root
                for ch in word[start:]:      
                    node = node.children[ch]
                    node.words.add(i)
        shortest = [""] * len(arr)
        self.dfs(root, "", shortest)
        return shortest 

    def dfs(self, node: Trie, path: str, shortest: List[str]):
        if len(node.words) == 1:
            word_idx = next(iter(node.words))
            if (shortest[word_idx] == "" or 
                len(path) < len(shortest[word_idx]) or 
                (len(path) == len(shortest[word_idx]) and path < shortest[word_idx])):
                shortest[word_idx] = path

        for ch in sorted(node.children.keys()):
            self.dfs(node.children[ch], path + ch, shortest)


            
