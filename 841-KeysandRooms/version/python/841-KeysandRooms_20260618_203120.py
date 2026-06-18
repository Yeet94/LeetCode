# Last updated: 6/18/2026, 8:31:20 PM
1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        To_visit = [0]
4        Visited = set()
5
6        while To_visit:
7            room_number = To_visit.pop()
8            
9            if room_number not in Visited:
10                Visited.add(room_number)
11
12                for keys in rooms[room_number]:
13                    To_visit.append(keys)
14        
15        return len(Visited) == len(rooms)