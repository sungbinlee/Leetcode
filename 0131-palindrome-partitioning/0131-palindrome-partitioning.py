class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start, path):
            # base case
            if start == len(s):
                ans.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                if self.isPalindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()        
        
        ans = []
        backtrack(0, [])
        return ans
        
    def isPalindrome(self, s):
        return s == s[::-1]