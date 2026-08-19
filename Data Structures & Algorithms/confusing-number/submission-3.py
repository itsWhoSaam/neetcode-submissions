class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
    
        # 1. Reject immediately if it contains 2, 3, 4, 5, or 7
        forbidden = {'2', '3', '4', '5', '7'}
        for char in s:
            if char in forbidden:
                return False
                
        # 2. Check if the string is a palindrome
        is_palindrome = True
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length - 1 - i]:
                is_palindrome = False
                break
                
        # 3. Check if all characters belong to {'0', '1', '8'}
        allowed_pal_digits = {'0', '1', '8'}
        only_180 = True
        for char in s:
            if char not in allowed_pal_digits:
                only_180 = False
                break
        
        # If it is a palindrome made of 1, 8, and 0 -> return False
        if is_palindrome and only_180:
            return False
            
        # Otherwise, return True
        return True