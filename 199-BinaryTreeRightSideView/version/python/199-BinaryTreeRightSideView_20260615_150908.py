# Last updated: 6/15/2026, 3:09:08 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
10        if not root:
11            return None
12        
13        queue = deque([root])
14        max_sum = root.val
15        max_level = 1
16        current_level = 0
17        while queue:
18            level_queue = len(queue)
19            level_sum = 0
20            current_level += 1
21            for count in range(level_queue):
22                node = queue.popleft()
23                level_sum += node.val
24                if node.left:
25                    queue.append(node.left)
26                if node.right:
27                    queue.append(node.right)
28            if level_sum > max_sum:
29                max_sum = level_sum
30                max_level = current_level
31
32        return max_level