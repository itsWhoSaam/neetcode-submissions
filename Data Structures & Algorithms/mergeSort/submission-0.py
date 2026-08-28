from typing import List

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(s: int, m: int, e: int) -> None:
            L = pairs[s : m + 1]
            R = pairs[m + 1 : e + 1]

            i = 0  # index for L
            j = 0  # index for R
            k = s  # index for pairs


            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    pairs[k] = L[i]
                    i += 1
                else:
                    pairs[k] = R[j]
                    j += 1
                k += 1


            while i < len(L):
                pairs[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                pairs[k] = R[j]
                j += 1
                k += 1

        def sort_helper(s: int, e: int) -> None:
            if e - s + 1 <= 1:
                return

            m = (s + e) // 2

            sort_helper(s, m)
            sort_helper(m + 1, e)
            merge(s, m, e)

        sort_helper(0, len(pairs) - 1)
        return pairs