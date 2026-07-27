# Last updated: 7/27/2026, 4:13:30 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
           fast = fast.next.next
           
           nxt = slow.next
           slow.next = prev
           prev = slow
           slow = nxt

        max_sum = 0
        while prev and slow:
            current_val = prev.val + slow.val
            max_sum = max(max_sum, current_val)
            prev = prev.next
            slow = slow.next
        
        return max_sum
        
