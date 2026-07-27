# Last updated: 7/27/2026, 4:13:38 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        current_height = 0
        for i, height in enumerate(gain):
            current_height += height
            max_height = max(max_height, current_height)
        
        return max_height
        