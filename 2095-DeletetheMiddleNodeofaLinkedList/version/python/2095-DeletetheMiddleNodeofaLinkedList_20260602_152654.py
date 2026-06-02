# Last updated: 6/2/2026, 3:26:54 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head == None:
9            return None
10        if head.next == None:
11            return head
12
13        odd = head
14        even = head.next
15        even_head = even
16
17        while even and even.next:
18            odd.next = even.next
19            odd = odd.next
20            even.next = odd.next
21            even = even.next
22        
23        odd.next = even_head
24        return head
25            