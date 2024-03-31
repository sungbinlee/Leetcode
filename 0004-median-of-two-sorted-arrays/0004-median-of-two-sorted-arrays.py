class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_num = sorted(nums1 + nums2)
        
        total_len = len(sorted_num)
        
        if total_len % 2 == 1:
            answer = sorted_num[len(sorted_num) // 2]
        else:
            answer = (sorted_num[(len(sorted_num) // 2) - 1] + sorted_num[len(sorted_num) // 2]) / 2
        
        return answer