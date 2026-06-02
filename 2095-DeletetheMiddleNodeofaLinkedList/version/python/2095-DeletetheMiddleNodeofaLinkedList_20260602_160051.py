# Last updated: 6/2/2026, 4:00:51 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next:
9            return head
10        
11        new_head = self.reverseList(head.next)
12        head.next.next = head
13        head.next = None
14
15        return new_head
16