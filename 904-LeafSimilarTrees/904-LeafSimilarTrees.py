# Last updated: 7/27/2026, 4:14:00 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            
            left_leaves = get_leaves(root.left)
            right_leaves = get_leaves(root.right)

            return left_leaves + right_leaves
        
        return get_leaves(root1) == get_leaves(root2)