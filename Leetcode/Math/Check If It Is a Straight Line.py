#https://leetcode.com/problems/check-if-it-is-a-straight-line/description/?envType=study-plan-v2&envId=programming-skills
from typing import List

def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    (x0,y0)=coordinates[0]
    (x1,y1)=coordinates[1]

    for x,y in coordinates:
        if(y1-y0)*(x-x0)-(y-y0)*(x1-x0):
            return False

    return True