# Last updated: 5/8/2026, 4:23:06 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case
        if not root:
            return False
        
        newSum = targetSum - root.val

        if not root.left and not root.right and newSum == 0:
            return True

        #since this is pre-order i will do the calculations first then recursively call. 

        return self.hasPathSum(root.left, newSum) or self.hasPathSum(root.right, newSum)

        