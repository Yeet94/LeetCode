# Last updated: 6/22/2026, 10:12:00 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack = []
4        curr_num = 0 
5        curr_string = ""
6
7        for char in s:
8            if char.isdigit():
9                curr_num = curr_num * 10 + int(char)
10                
11            elif char == '[':
12                stack.append([curr_num,curr_string])
13                curr_num = 0
14                curr_string = ""
15            
16            elif char == ']':
17                num, parent_string = stack.pop()
18                curr_string = parent_string + (curr_string * num)
19            
20            else:
21                curr_string += char
22        
23        return curr_string