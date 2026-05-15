class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for idx, curr in enumerate(nums):
            com = target - curr 
            if com in hmap:
                return [hmap[com], idx]
            hmap[curr] = idx

        