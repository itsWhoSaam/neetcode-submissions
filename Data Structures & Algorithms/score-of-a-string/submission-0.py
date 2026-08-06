class Solution:
    def scoreOfString(self, s: str) -> int:
        score_list = []
        n = len(s)
        i = 0
        j = 1
        while i < n and j < n:
            asci_1 = ord(s[i])
            asci_2 = ord(s[j])
            absolute_diff = abs(asci_1 - asci_2)
            score_list.append(absolute_diff)
            i += 1
            j += 1
        if len(score_list) == 1:
            return score_list[0]
        sum_total = 0
        for score in score_list:
            sum_total += score
        return sum_total

        