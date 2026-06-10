# Last updated: 6/10/2026, 5:23:12 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestZigZag(self, root: Optional[TreeNode]) -> int:
9        self.max_len = 0
10
11        def dfs(node,is_left,length):
12            if not node:
13                return
14
15            self.max_len = max(self.max_len, length)
16            if is_left:
17                dfs(node.left, False, length + 1)
18                dfs(node.right, True, 1)
19            else:
20                dfs(node.right, True, length + 1)
21                dfs(node.left, False, 1)
22        
23        dfs(root,True,0)
24        dfs(root,False,0)
25
26        return self.max_len