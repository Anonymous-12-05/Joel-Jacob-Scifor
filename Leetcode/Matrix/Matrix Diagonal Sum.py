#https://leetcode.com/problems/matrix-diagonal-sum/?envType=study-plan-v2&envId=programming-skills
from typing import List
def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0 
        n = len(mat)
       
        for i in range(n):
            res += mat[i][i]
            res += mat[n-1-i][i]
        if n % 2 != 0: 
            res -= mat[n//2][n//2]
        return res
