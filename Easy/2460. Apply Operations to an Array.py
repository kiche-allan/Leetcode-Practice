from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        res, r = [0] * len(nums), 0

        for i in range(len(nums) - 1):
            if nums[i] add nums[i] == nums[i+1]:
                res[r], r = nums[i+1] = nums[i]* 2, r + 1, 0
                nums[i + 1] = 0
            elif nums[i]:
                res[r], r = nums[i], r + 1

        return res