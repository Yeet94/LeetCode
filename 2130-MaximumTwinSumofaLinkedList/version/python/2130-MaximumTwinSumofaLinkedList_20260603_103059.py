# Last updated: 6/3/2026, 10:30:59 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        arr = []
9        while head:
10            arr.append(head.val)
11            head = head.next
12        
13        left = 0
14        right = len(arr) - 1
15
16        max_sum = 0
17        while left < right:
18            curr_sum = arr[left] + arr[right]
19            max_sum = max(curr_sum,max_sum)
20            left +=1
21            right -=1
22        
23        return max_sum
24