class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(currStr, left, right):
            if len(currStr) == n*2:
                result.append("".join(currStr))
            if left < n:
                currStr.append("(")
                backtracking(currStr, left+1 , right)
                currStr.pop()
            if right < left:
                currStr.append(")")
                backtracking(currStr, left , right+1)
                currStr.pop()
        backtracking([], 0, 0)
        return result

        
        

        