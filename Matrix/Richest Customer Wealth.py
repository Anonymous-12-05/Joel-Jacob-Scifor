#https://leetcode.com/problems/richest-customer-wealth/?envType=study-plan-v2&envId=programming-skills
from typing import List
def maximumWealth(self, accounts: List[List[int]]) -> int:
    maxx=0
    for i in accounts:
        add=0
        for k in i:
            add=add + k
        if maxx < add:
            maxx = add
    return maxx