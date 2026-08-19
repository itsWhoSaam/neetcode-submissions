class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] == strs[j][i]:
                    continue
                else:
                    if i == 0:
                        return common_prefix
                    common_prefix += (strs[0][:i])
                    return common_prefix

        if len(strs) == 0:
            return common_prefix
        
        

