# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegree = {}
        res = []

        for i,j in enumerate(recipes):
            indegree[j] = len(ingredients[i])
            for u in ingredients[i]:
                adj[u].append(j)
        q = deque(supplies)

        while q:
            node = q.popleft()
            if node not in adj:
                continue
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
                    res.append(nei)
        return res


        