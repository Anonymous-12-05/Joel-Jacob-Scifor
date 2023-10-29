#https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/?envType=study-plan-v2&envId=programming-skills
from typing import List
def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff=arr[1]-arr[0]
        for i in range(1,len(arr)):
                if(arr[i]-arr[i-1]!=diff):
                        return False
        return True