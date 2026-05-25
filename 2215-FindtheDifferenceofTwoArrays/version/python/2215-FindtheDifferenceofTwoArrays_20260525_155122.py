# Last updated: 5/25/2026, 3:51:22 PM
1
2class Solution:
3    def closeStrings(self, word1: str, word2: str) -> bool:
4        freq1 = [0] * 26
5        freq2 = [0] * 26
6
7        for ch in word1:
8            freq1[ord(ch) - ord('a')] += 1
9
10        for ch in word2:
11            freq2[ord(ch) - ord('a')] += 1
12
13        for i in range(26):
14            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
15                return False
16
17        freq1.sort()
18        freq2.sort()
19
20        for i in range(26):
21            if freq1[i] != freq2[i]:
22                return False
23
24        return True
25