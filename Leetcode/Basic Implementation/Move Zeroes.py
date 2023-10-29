#https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=programming-skills
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]

            # wait while we find a non-zero element to
            # swap with you
            if nums[j] != 0:
                j += 1
        