# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        dis = 0
        graph = {}
        queue = deque()
        queue.append(root)
        visited = {}

        while queue:
            n = len(queue)
            for _ in range(n):
                top = queue.popleft()

                if top.left:
                    graph[top.left.val] = top
                    queue.append(top.left)

                if top.right:
                    graph[top.right.val] = top
                    queue.append(top.right)
            
        queue.append(target)
        while dis < k and queue:
            n = len(queue)

            for _ in range(n):
                top = queue.popleft()
                visited[top.val] = 1
                if top.left and top.left.val not in visited:
                    queue.append(top.left)

                if top.right and top.right.val not in visited:
                    queue.append(top.right)

                if top.val in graph and graph[top.val].val not in visited:
                    queue.append(graph[top.val])
                    
            dis += 1
        while queue:
            res.append(queue.popleft().val)
            
        return res
