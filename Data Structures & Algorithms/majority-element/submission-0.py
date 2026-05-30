class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        max = 0
        maxk = 0
        for key, val in dict.items():
            if dict[key] > max:
                max = dict[key]
                maxk = key
        return maxk
        