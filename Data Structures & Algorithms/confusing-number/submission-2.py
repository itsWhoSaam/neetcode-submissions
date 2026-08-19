class Solution:
    def confusingNumber(self, n: int) -> bool:
        n_str = str(n)
        length = len(n_str)
        invalid_nums = {"2", "3", "4", "5", "7"}
        allowed = {"1", "8", "0"}
        
        for char in n_str:
            if char in invalid_nums:
                return False
            elif char == "6" or char == "9":
                return True
        for i in range(length//2):

            left_char = n_str[i]
            right_char = n_str[length - 1 - i]

            if left_char not in allowed or right_char not in allowed:
                return False

            if left_char != right_char:
                return False
        if n % 2 != 0:
            center_char = n_str[length // 2]
            if center_char not in allowed:
                return False
        return False