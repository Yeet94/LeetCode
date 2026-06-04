# Last updated: 6/4/2026, 10:41:45 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        self.max_depth = 0
10
11        def dfs(node,current_depth):
12            if not node:
13                self.max_depth = max(self.max_depth,current_depth)
14                return
15
16            dfs(node.left, current_depth + 1)
17            dfs(node.right, current_depth + 1)
18
19        dfs(root,0)
20
21        return self.max_depth        