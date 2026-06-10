# Last updated: 6/10/2026, 5:18:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestZigZag(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11
12        max_len = 0
13        stack = [(root,True,0), (root,False,0)]
14        while stack:
15            node , is_left, length = stack.pop()
16            if not node:
17                continue
18            
19            max_len = max(length,max_len)
20
21            if is_left:
22                stack.append((node.left, False, length + 1))
23                stack.append((node.right,True,1))
24            else:
25                stack.append((node.right,True,length+1))
26                stack.append((node.left,False,1))
27            
28        return max_len
29