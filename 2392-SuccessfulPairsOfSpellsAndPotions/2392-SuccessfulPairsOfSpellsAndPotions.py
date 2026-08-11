# Last updated: 8/11/2026, 12:01:39 PM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        length = len(potions)

        for i in range(len(spells)):
            left = 0
            right = length-1
            idx = length

            while left <= right:
                mid = left + (right-left)//2
                res = spells[i] * potions[mid]
                
                if res >= success:
                    idx = mid
                    right = mid - 1

                else:
                    left = mid + 1
            
            pairs.append(length-idx)
        
        return pairs

