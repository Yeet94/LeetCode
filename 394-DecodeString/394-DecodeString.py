# Last updated: 7/27/2026, 4:14:17 PM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0 
        curr_string = ""

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
                
            elif char == '[':
                stack.append([curr_num,curr_string])
                curr_num = 0
                curr_string = ""
            
            elif char == ']':
                num, parent_string = stack.pop()
                curr_string = parent_string + (curr_string * num)
            
            else:
                curr_string += char
        
        return curr_string