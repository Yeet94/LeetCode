# Last updated: 7/27/2026, 4:13:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def is_good(root, max_num):
            if not root:
                return 0

            current_score = 0
            if root.val >= max_num:
                max_num = root.val
                current_score = 1
            
            left_score = is_good(root.left,max_num)
            right_score = is_good(root.right,max_num)

            return current_score + left_score + right_score
        
        return is_good(root,root.val)
            
            
