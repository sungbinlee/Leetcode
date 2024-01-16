from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(s)
        count.subtract(Counter(t))
        
        return sum([abs(i) for i in count.values()])
        
        