class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s) == 0:
            if len(t) != 0:
                return True
        while i < len(t):
            if t[i]==s[j]:
                j += 1
                i += 1
            elif t[i] != s[j]:
                i += 1
        if j == len(s):
            return True
        return False
