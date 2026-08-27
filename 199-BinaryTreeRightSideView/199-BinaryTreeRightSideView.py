# Last updated: 8/27/2026, 11:16:18 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11
12        result = []
13        queue = deque([root])
14
15        while queue:
16            level_size = len(queue)
17
18            for i in range(level_size):
19                node = queue.popleft()
20
21                if i == level_size - 1:
22                    result.append(node.val)
23
24                if node.left:
25                    queue.append(node.left)
26
27                if node.right:
28                    queue.append(node.right)
29
30        return result