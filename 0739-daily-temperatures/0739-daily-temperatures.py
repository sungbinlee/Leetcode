class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures 어레이는 일일온도 담겨있음
        # 얼마나 기다려야 따뜻해지는지 담긴 배열 반환, 따뜻해질 예정 없으면 값 0 
        
        answer = [0] * len(temperatures)
        
        stack = []
        
        for cur_d, cur_t in enumerate(temperatures):
            while stack and stack[-1][1] < cur_t:
                prev_d, _ = stack.pop()
                answer[prev_d] = cur_d - prev_d 
            
            stack.append((cur_d, cur_t))
            
        return answer
        
        
        
        
       
