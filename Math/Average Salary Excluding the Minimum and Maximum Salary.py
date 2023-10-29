#https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/?envType=study-plan-v2&envId=programming-skills
from typing import List
def average(self, salary: List[int]) -> float:
    salary.sort()
    avg=0
    for i in range(1,len(salary)-1):
        avg+=salary[i]

    avg=avg/(len(salary)-2)

    return avg