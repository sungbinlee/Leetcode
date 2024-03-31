class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_num = []
        
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_num.append(nums1[i])
                i += 1
            else:
                sorted_num.append(nums2[j])
                j += 1
                
        while i < len(nums1):
            sorted_num.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            sorted_num.append(nums2[j])
            j += 1
        
        
        total_len = len(sorted_num)
        
        if total_len % 2 == 1:
            answer = sorted_num[len(sorted_num) // 2]
        else:
            answer = (sorted_num[(len(sorted_num) // 2) - 1] + sorted_num[len(sorted_num) // 2]) / 2
        
        return answer