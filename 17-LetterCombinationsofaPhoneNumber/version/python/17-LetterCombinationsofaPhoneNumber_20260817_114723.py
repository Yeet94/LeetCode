# Last updated: 8/17/2026, 11:47:23 AM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        digit_to_letters = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
4
5        if not digits:
6            return
7
8        combination = [""]
9        for digit in digits:
10            new_combination = [] 
11            for combo in combination:
12                for letter in digit_to_letters[digit]:
13                    new_combination.append(combo + letter)
14            
15            combination = new_combination
16
17        return combination