# Last updated: 7/27/2026, 4:13:45 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        count = 0
        left = 0
        max_vowel = 0

        for right in range(len(s)):
            if s[right] in vowels:
                count +=1
            if (right-left+1) ==k:
                max_vowel = max(count,max_vowel)
                if s[left] in vowels:
                    count -=1
                left+=1

        return max_vowel