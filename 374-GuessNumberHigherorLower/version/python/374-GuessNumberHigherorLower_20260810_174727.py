# Last updated: 8/10/2026, 5:47:27 PM
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        
11        if n < 2:
12            return n
13        
14        left = 1
15        right = n
16
17        while left <= right:
18            mid = left + (right-left)//2
19            res = guess(mid) 
20            if res == -1:
21                right = mid - 1
22            elif res == 1:
23                left = mid + 1
24            else:
25                return mid
26                
27    
28    