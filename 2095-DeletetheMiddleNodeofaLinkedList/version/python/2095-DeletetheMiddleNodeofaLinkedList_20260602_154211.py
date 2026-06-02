# Last updated: 6/2/2026, 3:42:11 PM
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
11        curr = head
12        arr = []
13        while curr:
14            arr.append(curr.val)
15            curr = curr.next
16        
17        dummy = ListNode(0)
18        current_node = dummy
19        for val in arr[::-1]:
20            current_node.next = ListNode(val)
21            current_node = current_node.next
22        
23        return dummy.next
24        
25
26