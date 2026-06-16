# Last updated: 6/16/2026, 12:14:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
9        if not root:
10            return None
11
12
13        if key > root.val:
14           root.right = self.deleteNode(root.right,key)
15        elif key < root.val:
16            root.left = self.deleteNode(root.left,key)
17        else:
18            #case1 no children
19            if not root.left and not root.right:
20                return None
21
22            #case2 one children
23            if not root.left:
24                return root.right
25            
26            if not root.right:
27                return root.left
28            
29            #case3 two children
30            successor = root.right
31            while successor.left:
32                successor = successor.left
33            
34            root.val = successor.val
35            
36            root.right = self.deleteNode(root.right,successor.val)
37        
38        return root
39
40            