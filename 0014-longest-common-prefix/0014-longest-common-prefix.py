class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""  # If the list is empty, there's no common prefix

        min_length = len(min(strs, key=len))
        
        for i in range(min_length):
            current_char = strs[0][i]
            for string in strs[1:]:
                if string[i] != current_char:
                    return strs[0][:i]
        return strs[0][:min_length] 