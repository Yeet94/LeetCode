# Last updated: 5/28/2026, 4:13:26 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        res = []
4        for i in (asteroids):
5            alive = True
6            while res and i < 0 and res[-1] > 0:
7                if abs(i) > res[-1]:
8                    res.pop()
9                elif abs(i) == res[-1]:
10                    res.pop()
11                    alive = False
12                    break
13                else:
14                    alive = False
15                    break
16
17            if alive:
18                res.append(i)
19        
20        return res