class Solution:
    def isValid(self, s: str) -> bool:
        flag = False 
        n = len(s)
        for i in range (0, n):
            if ((s[i] == '(' and  s[n - i - 1] == ')') or (s[i] == '[' and  s[n - i - 1] == ']') or (s[i] == '{' and  s[n - i - 1] == '}')):
                flag = True
        return flag