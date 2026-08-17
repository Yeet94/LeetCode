# Last updated: 8/17/2026, 1:25:09 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        digit_to_letters = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
4
5        if not digits:
6            return
7
8        result = []
9
10        def backtrack(index: int,path : str):
11            if index == len(digits):
12                result.append(path)
13                return
14
15
16            current_digit = digits[index]
17            for letter in digit_to_letters[current_digit]:
18                backtrack(index + 1, path + letter)
19
20        
21        backtrack(0,"")
22        return result