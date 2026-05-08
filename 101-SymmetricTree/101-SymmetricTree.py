# Last updated: 5/8/2026, 4:23:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root.left,root.right)]) 

        while queue:
            pair = queue.popleft()
            p = pair[0]
            q = pair[1]

            if not p and not q:
                continue
            
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            queue.append([p.left,q.right])
            queue.append([p.right,q.left])
        
        return True