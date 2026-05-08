# Last updated: 5/8/2026, 4:22:48 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []


        max_candies = max(candies)


        for candy in candies:
            total = candy + extraCandies


            if total >= max_candies:
                result.append(True)
            else:
                result.append(False)


        return result
           
