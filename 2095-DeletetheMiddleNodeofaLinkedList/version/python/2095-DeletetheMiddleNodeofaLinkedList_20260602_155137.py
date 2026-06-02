# Last updated: 6/2/2026, 3:51:37 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return None
10
11        pre = None
12        curr = head
13
14        while curr:
15            nxt = curr.next
16            curr.next = pre
17            pre = curr
18            curr = nxt
19        
20        return pre
21