class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # string 에서 알파베티칼 최대 연속된 s의 길이 반환
        
        cur = 1
        res = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
                
        return res
        
        
        