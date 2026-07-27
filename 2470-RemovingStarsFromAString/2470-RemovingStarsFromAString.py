# Last updated: 7/27/2026, 4:13:29 PM
class Solution:
    def removeStars(self, s: str) -> str:
        s_list = list(s)
        write = 0

        for read in range(len(s_list)):
            if s_list[read] == "*":
                write -= 1
            else:
                s_list[write] = s_list[read]
                write += 1
            
        return "".join(s_list[:write])