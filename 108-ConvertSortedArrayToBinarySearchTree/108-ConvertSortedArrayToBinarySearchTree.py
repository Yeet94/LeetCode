# Last updated: 5/8/2026, 4:23:11 PM
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.pointer = 0

        def build(indexA, indexB):
            if indexA > indexB:
                return None
            
            mid = (indexA + indexB)//2
            left_child = build(indexA, mid-1)

            val = nums[self.pointer]
            node = TreeNode(val)
            node.left = left_child

            self.pointer += 1
            node.right = build(mid+1, indexB)

            return node
        return build(0,len(nums)-1) 
