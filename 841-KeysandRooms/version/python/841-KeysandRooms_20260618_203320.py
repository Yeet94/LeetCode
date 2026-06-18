# Last updated: 6/18/2026, 8:33:20 PM
1from collections import deque
2
3
4class Solution:
5    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
6        visited = {0}
7        queue = deque([0])
8
9        while queue:
10            current_key = queue.popleft()
11
12            for key in rooms[current_key]:
13                if key not in visited:
14                    visited.add(key)
15                    queue.append(key)
16
17        return len(visited) == len(rooms)