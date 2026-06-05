# Last updated: 6/5/2026, 5:05:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        
10        def get_leaves(root):      
11            if not root:
12                return []
13            if not root.left and not root.right:
14                return [root.val]
15
16            left_leaves_val = get_leaves(root.left)
17            right_leaves_val = get_leaves(root.right)
18
19            return left_leaves_val + right_leaves_val
20        
21        return get_leaves(root1) == get_leaves(root2)
22
23        