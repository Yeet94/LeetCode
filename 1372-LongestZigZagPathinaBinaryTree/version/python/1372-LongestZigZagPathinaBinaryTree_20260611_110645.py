# Last updated: 6/11/2026, 11:06:45 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        stack = [root]
11        parent_map = {root:None}
12        while p not in parent_map or q not in parent_map:
13            node = stack.pop()
14
15            if node.left:
16                parent_map[node.left] = node
17                stack.append(node.left)
18
19            if node.right:
20                parent_map[node.right] = node
21                stack.append(node.right)
22
23        p_ancestors = []
24        while p:
25            p_ancestors.append(p)
26            p = parent_map[p]
27
28        q_ancestors = set()
29        while q:
30            q_ancestors.add(q)
31            q = parent_map[q]
32
33        for ancestor in p_ancestors:
34            if ancestor in q_ancestors:
35                return ancestor
36        
37        
38        
39
40                