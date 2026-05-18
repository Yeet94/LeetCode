# Last updated: 5/18/2026, 12:35:26 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        vowels = {"a","e","i","o","u"}
4        count = 0
5        left = 0
6        max_vowel = 0
7
8        for right in range(len(s)):
9            if s[right] in vowels:
10                count +=1
11            if (right-left+1) ==k:
12                max_vowel = max(count,max_vowel)
13                if s[left] in vowels:
14                    count -=1
15                left+=1
16
17        return max_vowel