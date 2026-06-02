# Last updated: 6/2/2026, 1:39:24 PM
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
11        pt = head
12        count = 0
13        while pt:
14            pt = pt.next
15            count += 1
16        
17        mid = count//2
18
19        curr = head
20        track = 0
21        while track < mid-1:
22            curr = curr.next
23            track +=1
24        
25        pre = curr
26        curr = curr.next.next
27        pre.next = curr
28
29        return head