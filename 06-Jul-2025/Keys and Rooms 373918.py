# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set()

        while q:
            room = q.popleft()

            if room not in visited:
                visited.add(room)
                for i in rooms[room]:
                    q.append(i)

        return len(visited) == len(rooms)
