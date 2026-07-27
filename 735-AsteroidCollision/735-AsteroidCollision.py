# Last updated: 7/27/2026, 4:14:04 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in (asteroids):
            alive = True
            while res and i < 0 and res[-1] > 0:
                if abs(i) > res[-1]:
                    res.pop()
                elif abs(i) == res[-1]:
                    res.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break

            if alive:
                res.append(i)
        
        return res