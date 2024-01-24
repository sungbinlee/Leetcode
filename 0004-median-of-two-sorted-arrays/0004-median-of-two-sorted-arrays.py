class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        sorted_nums = []
        
        i, j = 0, 0
        while i < len(nums1) and j <len(nums2):
            if nums1[i] < nums2[j]:
                sorted_nums.append(nums1[i])
                i += 1
            else:
                sorted_nums.append(nums2[j])
                j += 1
                
        while i < len(nums1):
            sorted_nums.append(nums1[i])
            i += 1
            
        while j < len(nums2):
            sorted_nums.append(nums2[j])
            j += 1
        
        total_len = len(sorted_nums)
        
        if total_len % 2 == 1:
            return sorted_nums[len(sorted_nums) // 2]
        else:
            return (sorted_nums[(len(sorted_nums) // 2) - 1] + sorted_nums[(len(sorted_nums) // 2)]) / 2