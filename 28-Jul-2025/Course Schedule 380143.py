# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        g = [[] for i in range(numCourses)]
        res = []
        
        for u,v in prerequisites: 
            g[u].append(v)
            indeg[v] += 1
        q = deque(i for i in range(numCourses) if indeg[i] == 0)

        while q:
            course = q.popleft()
            res.append(course)
            for nei in g[course]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        if len(res) != numCourses:
            return False
        return True
