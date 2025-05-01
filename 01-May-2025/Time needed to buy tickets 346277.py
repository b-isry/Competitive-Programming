# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        q = deque()
        for i in range(len(tickets)):
            q.append(i)

        while q:
            idx = q.popleft()
            tickets[idx] -= 1
            time += 1
            if idx == k and tickets[idx] == 0:
                return time
            if tickets[idx] > 0:
                q.append(idx)