# Last updated: 8/17/2026, 2:06:31 PM
1class Solution:
2    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
3        ans = []
4        stack = [(1,[],n)]
5
6        while stack:
7            start,path,remain_sum = stack.pop()
8
9            if len(path) == k and remain_sum == 0:
10                ans.append(path)
11
12            elif len(path) == k and remain_sum < 0:
13                pass
14            
15            else:
16                for i in range(start,10):
17                    if remain_sum - i >= 0:
18                        stack.append((i+1,path + [i], remain_sum - i))
19            
20        return ans
21                