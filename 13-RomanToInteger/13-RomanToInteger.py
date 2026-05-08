# Last updated: 5/8/2026, 4:23:43 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1, 
            "V":5, 
            "X":10, 
            "L":50, 
            "C":100, 
            "D":500, 
            "M":1000
        }

        total_sum = 0
        for i in range(len(s)):
            current_val = roman[s[i]]
            
            if i+1 < len(s):
                next_val = roman[s[i+1]]
                if current_val < next_val:
                    total_sum -= current_val
                else:
                    total_sum += current_val
            else:
                total_sum += current_val
        
        return total_sum