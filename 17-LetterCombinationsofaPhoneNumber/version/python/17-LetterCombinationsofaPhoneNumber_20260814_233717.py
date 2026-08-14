# Last updated: 8/14/2026, 11:37:17 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        digit_to_letters = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
4        if not digits:
5            return []
6
7        combinations = [""]
8
9        for digit in digits:
10            new_combinations = []
11            for combo in combinations:
12                for letter in digit_to_letters[digit]:
13                    new_combinations.append(combo + letter)
14
15            combinations = new_combinations
16
17        return combinations