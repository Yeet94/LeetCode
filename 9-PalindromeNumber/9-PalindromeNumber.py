# Last updated: 5/8/2026, 4:23:45 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x%10 ==0 and x != 0:
            return False

        reverse_half = 0
        xcopy = x
        while x>0:
            reverse_half = reverse_half*10 + x%10
            x //= 10
        return reverse_half == xcopy
