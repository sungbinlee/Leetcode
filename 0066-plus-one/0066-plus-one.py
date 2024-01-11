class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""
        for i in digits:
            temp += str(i)
        
        number = int(''.join(temp)) + 1
        return map(int,list(str(number)))