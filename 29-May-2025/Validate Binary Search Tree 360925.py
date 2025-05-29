# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if root is None:
                return True

            if not (lower < root.val < upper): 
                return False
            return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)

        return helper(root)
            
            