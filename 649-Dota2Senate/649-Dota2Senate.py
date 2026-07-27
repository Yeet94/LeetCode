# Last updated: 7/27/2026, 4:14:07 PM
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad_queue = deque()
        dire_queue = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                rad_queue.append(i)
            else:
                dire_queue.append(i)

        while rad_queue and dire_queue:
            rad_num = rad_queue.popleft()
            dire_num = dire_queue.popleft()

            if rad_num < dire_num:
                rad_queue.append(len(senate) + rad_num)
            else:
                dire_queue.append(len(senate) + dire_num)
        
        return "Radiant" if rad_queue else "Dire"