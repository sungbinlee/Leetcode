class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs += char.lower()
        
        while(len(strs) > 1):
            if strs.pop(0) != strs.pop():
                return False
        return True
                
