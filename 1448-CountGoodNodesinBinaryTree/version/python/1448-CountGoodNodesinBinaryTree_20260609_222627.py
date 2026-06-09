# Last updated: 6/9/2026, 10:26:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        def is_good(root, max_num):
10            if not root:
11                return 0
12
13            current_score = 0
14            if root.val >= max_num:
15                max_num = root.val
16                current_score = 1
17            
18            left_score = is_good(root.left,max_num)
19            right_score = is_good(root.right,max_num)
20
21            return current_score + left_score + right_score
22        
23        return is_good(root,root.val)
24            
25            
26