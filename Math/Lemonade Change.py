#https://leetcode.com/problems/lemonade-change/?envType=study-plan-v2&envId=programming-skills\
from typing import List
def lemonadeChange(self, bills: List[int]) -> bool:
        d={5:0,10:0}
        i=0
        while(i<len(bills)):
            current=bills[i]
            if current==5:
                d[5]+=1
            elif current==10:
                if d[5]!=0:
                    d[5]-=1
                    d[10]+=1
                else:
                    return False
            else:
                if (d[10]!=0 and d[5]!=0):
                    d[10]-=1
                    d[5]-=1
                elif d[5]>=3:
                    d[5]-=3
                else:
                    return False
            i+=1
        return True 