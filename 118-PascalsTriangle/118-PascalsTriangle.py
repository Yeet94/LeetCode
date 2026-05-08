# Last updated: 5/8/2026, 4:23:03 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]

        for i in range(1,numRows):
            dummyRow = [0] + res[-1] +[0]
            curr_row = []

            for j in range(i+1):
                curr_row.append(dummyRow[j]+dummyRow[j+1])

            res.append(curr_row)

        return res