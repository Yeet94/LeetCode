# Last updated: 6/16/2026, 11:29:29 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        stack = [root]
10        while stack:
11            node = stack.pop()
12            if node.val == val:
13                break
14            if node.left:
15                stack.append(node.left)
16            if node.right:
17                stack.append(node.right)
18
19
20        if node.val == val:
21            return node
22        else:
23            return None
24
25        