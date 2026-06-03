# Last updated: 6/3/2026, 10:51:30 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        slow = head
9        fast = head
10        prev = None
11
12        while fast and fast.next:
13           fast = fast.next.next
14           
15           nxt = slow.next
16           slow.next = prev
17           prev = slow
18           slow = nxt
19
20        max_sum = 0
21        while prev and slow:
22            current_val = prev.val + slow.val
23            max_sum = max(max_sum, current_val)
24            prev = prev.next
25            slow = slow.next
26        
27        return max_sum
28        
29