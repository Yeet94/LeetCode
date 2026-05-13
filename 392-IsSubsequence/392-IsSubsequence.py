# Last updated: 5/13/2026, 4:43:07 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dic = {}

        #Preprocess t
        for i,char in enumerate(t):
            if char not in dic:
                dic[char] = []
            dic[char].append(i)
        
        current_pos = -1
        for char in s:
            if char not in dic:
                return False
            
            next_idx = -1
            indicies = dic[char]

            l,r = 0, len(indicies)-1

            while l <= r:
                mid = (l+r)//2
                if indicies[mid] > current_pos:
                    next_idx = indicies[mid]
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            if next_idx == -1:
                return False
            
            current_pos = next_idx
        
        return True
        
