# Last updated: 7/27/2026, 4:13:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = deque([root])
        max_sum = root.val
        max_level = 1
        current_level = 0
        while queue:
            level_queue = len(queue)
            level_sum = 0
            current_level += 1
            for count in range(level_queue):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

        return max_level