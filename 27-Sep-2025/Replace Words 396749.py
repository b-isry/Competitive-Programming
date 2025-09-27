# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:
            node = root
            for ch in word:
                node = node.children[ch]  
            node.is_end = True
        
        sentence = sentence.split()
        for i in range(len(sentence)):
            node = root
            path = ''
            word = sentence[i]
            for ch in word:
                if ch not in node.children:
                    break
                node = node.children[ch]
                path += ch
                if node.is_end:
                    sentence[i] = path
                    break
        return " ".join(sentence)

