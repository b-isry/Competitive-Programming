# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, target, path):
            if node is None:
                return
            
            path.append(node.val)
            target -= node.val

            if node.left is None and node.right is None and target == 0:
                res.append(path[:]) 

            dfs(node.left, target, path)
            dfs(node.right, target, path)
            path.pop()

        dfs(root, targetSum, [])
        return res