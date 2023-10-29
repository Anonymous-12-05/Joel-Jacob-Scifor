#https://leetcode.com/problems/robot-return-to-origin/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d=dict()
        for i in moves:
            d[i]=d.get(i,0)+1
        if(d.get("U",0)==d.get("D",0) and d.get("L",0)==d.get("R",0)):
            return True
        return False