# Last updated: 6/16/2026, 11:34:01 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        curr = root
10
11        while curr:
12            if curr.val == val:
13                return curr
14            elif curr.val < val:
15                curr = curr.right
16            else:
17                curr = curr.left
18
19        return None
20        