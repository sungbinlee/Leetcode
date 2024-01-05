import re


class Solution:
    def romanToInt(self, s: str) -> int:
        
        s = re.sub("IV", "IIII", s)
        s = re.sub("IX", "IIIIIIIII", s)
        s = re.sub("XL", "XXXX", s)
        s = re.sub("XC", "XXXXXXXXX", s)
        s = re.sub("CD", "CCCC", s)
        s = re.sub("CM", "CCCCCCCCC", s)
        
        print(s)
        
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        answer = 0
        
        for i in s:
            answer += roman[i]
        
        return answer