# Last updated: 5/14/2026, 1:38:56 PM
1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        hashmap = {}
4        count = 0
5
6        for num in nums:
7            target = k - num
8            if hashmap.get(target, 0) > 0:
9                count +=1
10                hashmap[target] -=1
11            else:
12                hashmap[num] = hashmap.get(num,0) + 1
13
14        return count