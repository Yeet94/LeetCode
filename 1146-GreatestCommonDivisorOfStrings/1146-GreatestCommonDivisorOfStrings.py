# Last updated: 5/8/2026, 4:22:43 PM
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check if they share a common base pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Step 2: Find the GCD of the lengths
        # No need to check which is larger; the while loop handles the swap
        gcd_len = math.gcd(len(str1),len(str2))

        # Step 3: Return the prefix of that length
        return str1[:gcd_len]

        
                
            
