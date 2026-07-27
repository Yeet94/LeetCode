# Last updated: 7/27/2026, 4:14:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = {0 : 1}
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            
            needed_sum = current_sum - targetSum
            if needed_sum in prefix_sum:
                count = prefix_sum[needed_sum]
            else:
                count = 0
            
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1 


            count += dfs(node.left,current_sum)
            count += dfs(node.right,current_sum)
            
            prefix_sum[current_sum] -=1
            
            return count
        
        return dfs(root,0)



            
