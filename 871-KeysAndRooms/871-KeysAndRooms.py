# Last updated: 7/27/2026, 4:14:01 PM
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = {0}
        queue = deque([0])

        while queue:
            current_key = queue.popleft()

            for key in rooms[current_key]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == len(rooms)