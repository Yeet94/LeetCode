# Last updated: 6/9/2026, 10:03:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        if not root.left and not root.right:
10            return 1
11        
12        stack = [(root,root.val)]
13        count = 0
14        while stack:
15            curr, curr_max = stack.pop()
16            if curr.val >= curr_max:
17                count += 1
18                curr_max = curr.val 
19            
20            if curr.right:
21                stack.append((curr.right, curr_max))
22            if curr.left:
23                stack.append((curr.left, curr_max))
24                
25        return count