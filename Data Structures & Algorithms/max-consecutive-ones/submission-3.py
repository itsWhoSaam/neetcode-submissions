class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        current_streak = 0
        for x in nums:
            if x == 1:
                current_streak += 1
            else:
                # How should we handle current_streak here?
                current_streak = 0
            # Always keep track of the best we've seen
            max_val = max(max_val, current_streak)
        return max_val