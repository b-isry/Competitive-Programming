# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    longest = []
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(x, root):
            temp = root
            for i in range(x, len(word)):
                if word[i] == '.':
                    for child in temp.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in temp.children:
                        return False
                    temp = temp.children[word[i]]
            return temp.is_end
        return dfs(0, self.root)
