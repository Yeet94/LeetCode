# Last updated: 6/4/2026, 10:54:05 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        max_depth = 0
12        stack = [(root,1)]
13        while stack:
14            node,current_depth = stack.pop()
15            if node:
16                max_depth = max(max_depth,current_depth)
17
18                if node.left:
19                    stack.append((node.left, current_depth + 1))
20                if node.right:
21                    stack.append((node.right, current_depth + 1))
22
23        
24        return max_depth
25                