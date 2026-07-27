# Last updated: 7/27/2026, 4:13:51 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        return len(dic.values()) == len(set(dic.values()))

