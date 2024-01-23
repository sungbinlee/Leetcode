class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for curr_d, curr_t in enumerate(temperatures):
            while stack and stack[-1][1] < curr_t:
                prev_d, _ = stack.pop()
                answer[prev_d] = curr_d - prev_d
            stack.append((curr_d, curr_t))

        return answer