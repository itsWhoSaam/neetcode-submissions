class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1 and s[0] != " ":
            return len(s[0])
        word_list = s.split(" ")
        # print(word_list)
        for i in range(len(word_list) -1, -1, -1):
            # print(f"word_list[{i}]{word_list[i]}")
            if word_list[i] != "":
                return len(word_list[i])