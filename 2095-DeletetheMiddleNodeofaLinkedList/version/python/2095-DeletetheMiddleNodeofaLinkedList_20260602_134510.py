# Last updated: 6/2/2026, 1:45:10 PM
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
11        curr = head
12        total_nodes = 0
13        while curr:
14            total_nodes +=1
15            curr = curr.next
16        
17        mid = total_nodes//2
18
19        curr = head
20        
21        for _ in range(mid-1):
22            curr = curr.next
23        
24        curr.next = curr.next.next
25
26        return head