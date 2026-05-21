# Last updated: 5/21/2026, 4:18:49 PM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        max_height = 0
4        current_height = 0
5        for i, height in enumerate(gain):
6            current_height += height
7            max_height = max(max_height, current_height)
8        
9        return max_height
10        