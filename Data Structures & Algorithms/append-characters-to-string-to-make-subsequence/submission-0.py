class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = 0
        if len(t) == 1:
            return 0
        for i in range(len(t)):
            print("s[i]:", s[i], "t[i]:", t[i])
            if s[i] == t[i]:
                continue
            elif s[i] != t[i]:
                return int(len(t[i:]))
            
        
