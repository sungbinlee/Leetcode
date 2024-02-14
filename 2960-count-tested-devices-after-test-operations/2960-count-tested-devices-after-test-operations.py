class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        answer = 0
        for x in batteryPercentages:
            if answer < x: answer += 1
        return answer
    
    