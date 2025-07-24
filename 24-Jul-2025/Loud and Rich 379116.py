# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        indegree = [0] * n
        ans = [i for i in range(n)]

        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()

            for i in graph[curr]:
                curr_quiet = ans[curr]
                _quiet = ans[i]

                if quiet[curr_quiet] < quiet[_quiet]:
                    ans[i] = curr_quiet

                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return ans
  