# Last updated: 6/9/2026, 9:28:34 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        def get_leaves(root):
10            if not root:
11                return []
12            if not root.left and not root.right:
13                return [root.val]
14            
15            left_leaves = get_leaves(root.left)
16            right_leaves = get_leaves(root.right)
17
18            return left_leaves + right_leaves
19        
20        return get_leaves(root1) == get_leaves(root2)