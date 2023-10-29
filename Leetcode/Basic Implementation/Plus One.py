#https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=programming-skills
from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
    num=0
    x=0
    for i in digits:
        
        num=num*10+i
    
    num+=1

    ans=[]
    while(num>0):
            ans.append(num%10)
            num=num//10

    return ans[::-1]



