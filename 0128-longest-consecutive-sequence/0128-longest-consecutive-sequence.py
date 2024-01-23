class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 정렬되지 않은 정수가 담긴 nums 어레이가 주어졌을때
        # 연속되는 엘리먼츠의 길이를 반환하라
        # 시간복잡도 o(n) 으로 풀어야한다. 
        longest = 0
        nums_set = set()
        
        for num in nums:
            nums_set.add(num)
            
        print(nums_set)
            
        for num in nums_set:
            if num - 1 not in nums_set:
                cnt = 1
                target = num + 1
                while target in nums_set:
                    target += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest
        
        
    