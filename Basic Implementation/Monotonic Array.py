#https://leetcode.com/problems/monotonic-array/?envType=study-plan-v2&envId=programming-skills
from typing import List
def isMonotonic(self, nums: List[int]) -> bool:
        if (nums[-1]>nums[0]):
                for i in range(len(nums)-1):
                        if(nums[i+1]<nums[i]):
                                return False
        else:
                for i in range(len(nums)-1):
                        if(nums[i+1]>nums[i]):
                                return False
        return True