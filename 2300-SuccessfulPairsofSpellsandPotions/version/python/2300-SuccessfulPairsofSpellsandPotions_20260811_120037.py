# Last updated: 8/11/2026, 12:00:37 PM
1class Solution:
2    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
3        potions.sort()
4        pairs = []
5        length = len(potions)
6
7        for i in range(len(spells)):
8            left = 0
9            right = length-1
10            idx = length
11
12            while left <= right:
13                mid = left + (right-left)//2
14                res = spells[i] * potions[mid]
15                
16                if res >= success:
17                    idx = mid
18                    right = mid - 1
19
20                else:
21                    left = mid + 1
22            
23            pairs.append(length-idx)
24        
25        return pairs
26
27