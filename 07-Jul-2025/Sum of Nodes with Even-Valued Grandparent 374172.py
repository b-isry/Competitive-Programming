# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, p, gp):
            if not node:
                return 0

            ans = 0
            if gp and gp.val % 2 == 0:
                ans += node.val

            ans += dfs(node.left, node, p)
            ans += dfs(node.right, node, p)
            return ans

        return dfs(root, None, None)