#https://leetcode.com/problems/add-binary/description/?enremType=study-plan-rem2&enremId=programming-skills
from typing import List
def addBinary(self, a: str, b: str) -> str:
        inta = 0
        intb = 0
        for i in range(len(a)):
            inta +=int(a[i])*2**(len(a)-1-i)
        for i in range(len(b)):
            intb += int(b[i])*2**(len(b)-1-i)
        
        n = inta+intb
        result = ''
        if n !=0:
            while True:
                if n != 0:
                    rem = n%2
                    result = str(rem)+result
                else:
                    break
                n = n//2
            return result
        return '0'