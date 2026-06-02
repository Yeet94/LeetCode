# Last updated: 6/2/2026, 1:12:45 PM
1from collections import deque
2class Solution:
3    def predictPartyVictory(self, senate: str) -> str:
4        rad_queue = deque()
5        dire_queue = deque()
6
7        for i in range(len(senate)):
8            if senate[i] == "R":
9                rad_queue.append(i)
10            else:
11                dire_queue.append(i)
12
13        while rad_queue and dire_queue:
14            rad_num = rad_queue.popleft()
15            dire_num = dire_queue.popleft()
16
17            if rad_num < dire_num:
18                rad_queue.append(len(senate) + rad_num)
19            else:
20                dire_queue.append(len(senate) + dire_num)
21        
22        return "Radiant" if rad_queue else "Dire"