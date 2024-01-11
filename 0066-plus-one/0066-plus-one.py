class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = map(str, digits)
        number = int(''.join(temp)) + 1
        return map(int,list(str(number)))