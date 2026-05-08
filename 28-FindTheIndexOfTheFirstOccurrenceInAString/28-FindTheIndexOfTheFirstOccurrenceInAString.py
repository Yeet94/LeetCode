# Last updated: 5/8/2026, 4:23:31 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n: return -1
        
        # Constants for hashing
        base = 26  # Since we use lowercase a-z
        mod = 10**9 + 7 # A large prime to prevent overflow
        
        h_hash, n_hash = 0, 0
        power = 1 # base^(m-1)
        
        # Calculate initial hashes for needle and first window
        for i in range(m):
            n_hash = (n_hash * base + ord(needle[i])) % mod
            h_hash = (h_hash * base + ord(haystack[i])) % mod
            if i < m - 1:
                power = (power * base) % mod
        
        # Slide the window
        for i in range(n - m + 1):
            # If hashes match, verify characters (to handle collisions)
            if h_hash == n_hash:
                if haystack[i : i + m] == needle:
                    return i
            
            # Roll the hash to the next window
            if i < n - m:
                # Remove first char, shift, add next char
                h_hash = (base * (h_hash - ord(haystack[i]) * power) + ord(haystack[i + m])) % mod
        
        return -1


