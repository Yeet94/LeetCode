# Last updated: 5/8/2026, 4:23:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        L_H = self.checkHeight(root.left)
        R_H = self.checkHeight(root.right)

        if abs(L_H -R_H) >1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def checkHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1+max(self.checkHeight(node.left),self.checkHeight(node.right))
