class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def insertion_sort(array):
            for i in range(1, len(array)):
                for j in range(i, 0, -1):
                    if array[j] < array[j-1]:
                        array[j-1], array[j] = array[j], array[j-1]
                        
        insertion_sort(nums)
                
        
        
            
        