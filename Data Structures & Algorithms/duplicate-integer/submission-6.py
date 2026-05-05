class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
#method I
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False
#method II
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
#method III
        return len(nums) != len(set(nums))
        