# Last updated: 6/11/2026, 11:11:10 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if not root or root == p or root ==q:
11            return root
12        
13        left = self.lowestCommonAncestor(root.left,p,q)
14        right = self.lowestCommonAncestor(root.right,p,q)
15
16        if left and right:
17            return root
18        
19        return left if left else right
20
21        
22
23                