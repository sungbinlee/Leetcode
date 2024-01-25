class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        
        for i in nums1:
            flag = False
            
            i_index = nums2.index(i)
            windowed = nums2[i_index + 1:]
            for j in windowed:
                if j > i:
                    flag = True
                    stack.append(j)
                    break
            
            
        
            if flag == False:
                stack.append(-1)
            
        return stack