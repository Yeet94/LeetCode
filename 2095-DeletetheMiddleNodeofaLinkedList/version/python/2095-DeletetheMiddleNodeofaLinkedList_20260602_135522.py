# Last updated: 6/2/2026, 1:55:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head.next == None:
9            return None
10
11        slow = head
12        fast = head.next.next
13
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17
18        slow.next = slow.next.next
19        return head