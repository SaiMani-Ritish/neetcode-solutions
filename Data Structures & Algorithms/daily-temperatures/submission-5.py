class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n 

        for index,curr in enumerate(temperatures):
            while stack and curr > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = index - prev_day
            stack.append(index)
        return result
        