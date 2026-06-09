# Last updated: 6/9/2026, 10:54:22 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
9        prefix_sums = {0: 1}
10
11        def dfs(node,current_sum):
12            if not node:
13                return 0
14            
15            current_sum += node.val
16
17            needed_sum = current_sum - targetSum
18
19            if needed_sum in prefix_sums:
20                count = prefix_sums[needed_sum]
21            else:
22                count = 0
23            
24            if current_sum in prefix_sums:
25                prefix_sums[current_sum] += 1
26            else:
27                prefix_sums[current_sum] = 1
28
29            count += dfs(node.right, current_sum)
30            count += dfs(node.left, current_sum)
31
32            prefix_sums[current_sum] -= 1
33
34            return count
35
36    
37        return dfs(root, 0)