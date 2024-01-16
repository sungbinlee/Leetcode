from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_count = Counter(s)
        
        steps = 0
        
        for char in t:
            if char_count[char] > 0:
                char_count[char] -= 1
            else:
                steps += 1
                
        return steps
        