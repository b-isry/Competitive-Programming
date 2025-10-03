# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Trie:
    def __init__(self):
        self.children = {}   
        self.is_end = False  

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()

        for f in folder:
            node = root
            parts = f.split('/')[1:]  
            for part in parts:
                if part not in node.children:
                    node.children[part] = Trie()
                node = node.children[part]
            node.is_end = True

        result = []

        def dfs(node, path):
            if node.is_end:
                result.append(path)
                return
            for name, node in node.children.items():
                dfs(node, path + '/' + name)
        
        dfs(root, "")
        return result
                