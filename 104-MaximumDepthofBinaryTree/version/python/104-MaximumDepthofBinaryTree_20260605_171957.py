# Last updated: 6/5/2026, 5:19:57 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        def get_leaves_top_down(root,leaf_list):
10            if not root:
11                return
12            
13            if not root.left and not root.right:
14                leaf_list.append(root.val)
15                return
16            
17            get_leaves_top_down(root.left,leaf_list)
18            get_leaves_top_down(root.right,leaf_list)
19
20        leaves1 = []
21        leaves2 = []
22    
23        get_leaves_top_down(root1,leaves1)
24        get_leaves_top_down(root2,leaves2)
25
26        return leaves1 == leaves2
27        