# Last updated: 5/8/2026, 4:22:45 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2

        if not word2:
            return word1

        res = []
        pt = 0
        while pt < len(word1) and pt < len(word2):
            res.append(word1[pt])
            res.append(word2[pt])
            pt +=1

        if pt < len(word1):
            res.append(word1[pt::])
        else:
            res.append(word2[pt::])

        return "".join(res)