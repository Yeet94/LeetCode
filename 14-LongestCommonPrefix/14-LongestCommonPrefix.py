# Last updated: 5/8/2026, 4:23:41 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        reference = strs[0]
        for i, char in enumerate(reference):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return reference[:i]
        
        return reference