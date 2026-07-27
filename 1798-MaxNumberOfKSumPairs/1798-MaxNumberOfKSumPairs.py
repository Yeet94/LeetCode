# Last updated: 7/27/2026, 4:13:39 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0

        for num in nums:
            target = k - num
            if hashmap.get(target, 0) > 0:
                count +=1
                hashmap[target] -=1
            else:
                hashmap[num] = hashmap.get(num,0) + 1

        return count