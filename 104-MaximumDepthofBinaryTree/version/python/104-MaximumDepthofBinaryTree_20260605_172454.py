# Last updated: 6/5/2026, 5:24:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        def get_leaves_stack(root):
10            if not root:
11                return []
12            
13            leaves = []
14            stack = [root]
15
16            while stack:
17                curr = stack.pop()
18                if not curr.left and not curr.right:
19                    leaves.append(curr.val)
20
21                if curr.right:
22                    stack.append(curr.right)
23                
24                if curr.left:
25                    stack.append(curr.left)
26                
27            return leaves
28        
29        return get_leaves_stack(root1) == get_leaves_stack(root2)