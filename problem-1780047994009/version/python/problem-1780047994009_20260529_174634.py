# Last updated: 5/29/2026, 5:46:34 PM
1from collections import deque
2class Solution:
3    def predictPartyVictory(self, senate: str) -> str:
4        Rad_queue = deque()
5        Dire_queue = deque()
6        for i in range(len(senate)):
7            if senate[i] == "R":
8                Rad_queue.append(i)
9            else:
10                Dire_queue.append(i)
11
12        
13        while Rad_queue and Dire_queue:
14            Rad_num = Rad_queue.popleft()
15            Dire_num = Dire_queue.popleft()
16
17            if Rad_num < Dire_num:
18                Rad_queue.append(Rad_num + len(senate))
19            else:
20                Dire_queue.append(Dire_num + len(senate))
21
22            
23        return "Radiant" if Rad_queue else "Dire"
24