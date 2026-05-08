# Last updated: 5/8/2026, 4:22:52 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        
        left = 0
        right = len(s)-1

        s_list = list(s)

        while left < right:
            if s_list[left] not in vowels:
                left += 1
            elif s_list[right] not in vowels:
                right -= 1
            else:
                s_list[left],s_list[right] = s_list[right], s_list[left]
                left +=1
                right -=1
        
        return "".join(s_list)