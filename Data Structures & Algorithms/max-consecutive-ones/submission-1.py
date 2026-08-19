class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        fin_max_1s = 0
        max_1s = 1
        i = 0
        j = 1
        while j < len(nums):
            print("i: ", i, "j: ", j, "nums[",i,"]: ", nums[i], "nums[",j,"]: ", nums[j], max_1s)
            if nums[i] == 1 and nums[j] == 1:
                max_1s += 1
                i += 1
                j+= 1
                fin_max_1s = max_1s
            else:
                max_1s = 1
                i += 1
                j += 1
        return fin_max_1s

            
        