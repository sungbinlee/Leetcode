class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        sorted_nums = sorted(nums1 + nums2)
        
        total_len = len(sorted_nums)
        
        if total_len % 2 == 1:
            return sorted_nums[len(sorted_nums) // 2]
        else:
            return (sorted_nums[(len(sorted_nums) // 2) - 1] + sorted_nums[(len(sorted_nums) // 2)]) / 2