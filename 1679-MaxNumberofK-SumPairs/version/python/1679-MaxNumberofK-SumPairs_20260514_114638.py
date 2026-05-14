# Last updated: 5/14/2026, 11:46:38 AM
1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        hashmap = {}
4        for num in nums:
5            if num not in hashmap:
6                hashmap[num] = 1
7            else:
8                hashmap[num] += 1
9
10        count = 0
11        
12        for x in hashmap:
13            target = k - x
14            if hashmap[x] > 0 and target in hashmap and hashmap[target] > 0:
15
16                if x == target:
17                    count += hashmap[x]//2
18                    hashmap[x] == 0
19                
20                else:
21                    num_pairs = min(hashmap[x], hashmap[target])
22                    count += num_pairs
23
24                    hashmap[x] -= num_pairs
25                    hashmap[target] -= num_pairs
26
27        return count
28                
29
30