# Last updated: 5/8/2026, 4:23:29 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
        
        

        
