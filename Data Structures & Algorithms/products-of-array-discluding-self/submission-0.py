class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        for i in range(1,n):
            result[i] = result[i - 1] * nums[i - 1]

        right_product = 1
        for i in range(n - 1, -1 , -1):
            result[i] *= right_product
            right_product *= nums[i]
    
        return result


        # n = len(nums)
        # result = [1] * n

        # # Step 1: left products
        # for i in range(1, n):
        #     res[i] = res[i - 1] * nums[i - 1]

        # # Step 2: right products
        # right_product = 1
        # for i in range(n - 1, -1, -1):
        #     res[i] *= right_product
        #     right_product *= nums[i]

        # return res

        