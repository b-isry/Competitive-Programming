# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, path):
            nonlocal ans
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                curr = int("".join(map(str, path)))
                ans += curr
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return ans