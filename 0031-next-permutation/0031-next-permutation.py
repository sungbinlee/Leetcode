class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums)[::-1] == nums:
            nums.sort()
            return
   
        j = len(nums) - 1
        while j >= 0:
            if sorted(nums[j:])[::-1] != nums[j:]:
                lst =  sorted(nums[j:])
                q = 0
                while lst[q] <= nums[j]:
                    q += 1
                nums[j] = lst[q]
                lst = lst[:q] + lst[q+1:]
                for p in range(len(lst)):
                    nums[j+1+p] = lst[p]
                break
            j -= 1