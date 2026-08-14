# Last updated: 8/14/2026, 6:43:51 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        def can_finish(k):
4            hours = 0 
5            for pile in piles:
6                hours += pile//k
7
8                if pile % k != 0:
9                    hours += 1
10            return hours <= h
11
12        left , right = 1 , max(piles)
13
14        while left < right:
15            mid = (left+right) // 2
16            
17            if can_finish(mid):
18                right = mid
19            else:
20                # When left == right, we've found the minimum working speed
21                left = mid + 1
22        
23        return left
24
25        
26
27
28
29
30        
31
32                
33                    