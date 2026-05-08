# Last updated: 5/8/2026, 4:23:00 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 0: Clean spaces and convert to list
        # (In Python, this part is O(n), but the following logic is O(1) space)
        chars = list(" ".join(s.split()))
        n = len(chars)

        # 1. Reverse the entire array
        self.reverse_range(chars, 0, n - 1)

        # 2. Reverse each individual word
        start = 0
        for end in range(n + 1):
            # If we reach a space or the end of the list, we found a word boundary
            if end == n or chars[end] == ' ':
                self.reverse_range(chars, start, end - 1)
                start = end + 1

        return "".join(chars)

    def reverse_range(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1