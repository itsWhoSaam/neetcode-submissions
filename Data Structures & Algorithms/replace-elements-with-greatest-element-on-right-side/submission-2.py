class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if len(arr) == 1:
            arr[0] = -1
            return arr
        for i in range(1, n):
            arr[i-1] = max(arr[i:n])
            if i == n-1:
                arr[i] = -1
        return arr
        
        