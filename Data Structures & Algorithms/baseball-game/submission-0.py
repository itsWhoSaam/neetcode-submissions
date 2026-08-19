class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        i = 0
        j = 0
        for i in range(len(operations)):
            if (operations[i].isnumeric()):
                res.append(int(operations[i]))
                j+= 1
            elif operations[i] == "+":
                if j>0 and len(res)>= 2:
                    sum = res[j-1] + res[j-2]
                    res.append(sum)
                    j += 1
            elif operations[i] == "C":
                if len(res) != 0:
                    res.pop()
                    j-= 1

            elif operations[i] == "D":
                if j>0 and len(res)!=0:
                    double = res[j-1] * 2
                    res.append(double)
                    j+=1
        sum=0
        print(res)
        for i in range(len(res)):
            sum += res[i]
        return sum
