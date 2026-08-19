class Solution:
    def confusingNumber(self, n: int) -> bool:
        n_str = str(n)
        length = len(n_str)
        invalid_nums = ["2", "3", "4", "5", "7"]
        for i in range(length):
            if (n_str[i] == n_str[length - 1]) and (n_str == "1" or n_str == "8" or n_str == "0"):
                return False
        
        for char in n_str:
            if char in invalid_nums:
                return False
            elif char == "6" or char == "9":
                return True