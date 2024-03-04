class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i, v in enumerate(nums):
            dic[v] = i
            
        for i, v in enumerate(nums):
            complement = target - v
            if complement in dic and i is not dic[target-v]:
                return [i, dic[target-v]]