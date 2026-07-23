from functools import cmp_to_key
class Solution:
    def compare(self,a,b):
        if a + b > b + a:
            return -1
        else:
            return 1
    def largestNumber(self, nums: List[int]) -> str:
        # final = ""
        # nums_sorted_rev = nums.sort(reverse=True)

        list_of_strings = [str(x) for x in nums]
        sorted_list = sorted(list_of_strings, key=cmp_to_key(self.compare))
        res = "".join(sorted_list)

        return "0" if res[0] == "0" else res
        # for i in range(9, -1, -1):
            
        #     for char in list_of_strings:
        #         print("i:", i, "final: ", final, "char: ", char)
        #         if char.startswith(str(i)):
        #             final += char
        # return final

