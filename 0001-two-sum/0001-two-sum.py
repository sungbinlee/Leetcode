class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        
        for i, num in enumerate(nums):
            nums_hash[num] = i
        
        for i, num in enumerate(nums):
            if target - num in nums_hash and i != nums_hash[target-num]:
                return [i, nums_hash[target-num]]
            
            