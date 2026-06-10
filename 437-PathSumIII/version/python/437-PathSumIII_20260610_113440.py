# Last updated: 6/10/2026, 11:34:40 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
9        prefix_sum = {0 : 1}
10        
11        def dfs(node, current_sum):
12            if not node:
13                return 0
14            
15            current_sum += node.val
16            
17            needed_sum = current_sum - targetSum
18            if needed_sum in prefix_sum:
19                count = prefix_sum[needed_sum]
20            else:
21                count = 0
22            
23            if current_sum in prefix_sum:
24                prefix_sum[current_sum] += 1
25            else:
26                prefix_sum[current_sum] = 1 
27
28
29            count += dfs(node.left,current_sum)
30            count += dfs(node.right,current_sum)
31            
32            prefix_sum[current_sum] -=1
33            
34            return count
35        
36        return dfs(root,0)
37
38
39
40            
41