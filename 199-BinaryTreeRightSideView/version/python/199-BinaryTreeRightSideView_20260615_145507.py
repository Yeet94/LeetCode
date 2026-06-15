# Last updated: 6/15/2026, 2:55:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
10        if not root:
11            return []
12        
13        queue = deque([root])
14        res = []
15        while queue:
16            level_queue = len(queue)
17            for count in range(level_queue):
18                node = queue.popleft()
19                if count == level_queue-1:
20                    res.append(node.val)
21                if node.left:
22                    queue.append(node.left)
23                if node.right:
24                    queue.append(node.right)
25
26        return res