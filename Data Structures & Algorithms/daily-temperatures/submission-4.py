class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n 

        for idx,curr in enumerate(temperatures):
            while stack and curr > temperatures[stack[-1]]:
                prev_idx = stack.pop() 
                result[prev_idx] = idx - prev_idx
            stack.append(idx)
        return result