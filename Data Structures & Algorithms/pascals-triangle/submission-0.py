class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res
            # if i == 0:
            #     res.append([i + 1])
            # elif i == 1:
            #     res.append([i , i ])
            # elif i == 2:
            #     res.append([i-1, i , i-1])
            # elif i == 3:
            #     res.append([i-2, i, i, i-2])
            # elif i == 4:
            #     res.append([i-3, i, i+2, i, i-3])