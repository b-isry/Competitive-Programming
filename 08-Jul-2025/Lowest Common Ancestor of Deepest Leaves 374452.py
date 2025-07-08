# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return 0, None
            left_dep, left_node = dfs(node.left)
            right_dep, right_node = dfs(node.right)

            if left_dep > right_dep:
                return left_dep + 1, left_node
            elif right_dep > left_dep:
                return right_dep + 1, right_node
            else:
                return left_dep + 1, node

        return dfs(root)[1]
