class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = [0] * n 
        right_arr = [0] * n
        right_one = 1
        left_one = 1

        for i in range(n):
            j = -i -1
            left_arr[i] = left_one
            right_arr[j] = right_one
            left_one *= nums[i]
            right_one *= nums[j]

        return [left_arr[k] * right_arr[k] for k in range(n)]