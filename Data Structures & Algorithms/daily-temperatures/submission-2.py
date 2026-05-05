class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n 
        stack = []

        for index, heat in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < heat:
                prev_index = stack.pop()
                result[prev_index] = index - prev_index 
            stack.append(index)
        return result