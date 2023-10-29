#https://leetcode.com/problems/sign-of-the-product-of-an-array/description/?envType=study-plan-v2&envId=programming-skills
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cn=0
        for i in nums:
            if(i<0):
                cn+=1
            elif(i==0):
                return 0
        if(cn%2==0):
            return 1
        else:
            return -1