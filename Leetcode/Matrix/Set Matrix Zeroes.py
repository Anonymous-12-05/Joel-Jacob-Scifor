#https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=programming-skills
from typing import List
def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for row in range(n):
                        if matrix[i][row]!=0:
                            matrix[i][row]="a"
                    for col in range(m):
                        if matrix[col][j]!=0:
                            matrix[col][j]="a"

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==("a"):
                    matrix[i][j]=0
                