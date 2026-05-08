# Last updated: 5/8/2026, 4:23:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root,1)])
        while queue:
            node,height = queue.popleft()
            if not node.left and not node.right:
                return height
            
            if node.left:
                queue.append((node.left,height+1))

            if node.right:
                queue.append((node.right,height+1))
        
    

