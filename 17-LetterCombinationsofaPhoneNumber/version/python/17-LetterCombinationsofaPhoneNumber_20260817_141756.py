# Last updated: 8/17/2026, 2:17:56 PM
1class Solution:
2    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
3        
4        ans = []
5
6        def backtrack(start:int, path:list[int], target:int):
7
8            if len(path) == k and target == 0:
9                ans.append(path)
10                return
11            
12            elif len(path) == k and target < 0:
13                return
14
15            else:
16                for i in range(start,10):
17                    backtrack(i+1,path + [i], target - i)
18        
19        backtrack(1,[],n)
20        return ans