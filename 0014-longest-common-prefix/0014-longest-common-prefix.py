class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_length = len(min(strs, key=len))
        
        for i in range(min_length):
            curr = strs[0][i]
            
            for strings in strs[1:]:
                if strings[i] != curr:
                    return strs[0][:i]
            
        return strs[0][:min_length]
                
            
            