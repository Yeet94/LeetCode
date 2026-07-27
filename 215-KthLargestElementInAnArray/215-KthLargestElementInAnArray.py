# Last updated: 7/27/2026, 4:14:25 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[len(nums)//2]

        left = []
        middle = []
        right = []

        for x in nums:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)


        if k <= len(right):
            return self.findKthLargest(right,k)
        
        elif k <= len(middle) + len(right):
            return pivot

        else:
            new_k = k - len(middle) - len(right)
            return self.findKthLargest(left,new_k)