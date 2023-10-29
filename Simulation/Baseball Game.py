# https://leetcode.com/problems/baseball-game/description/?envType=study-plan-v2&envId=programming-skills
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in operations:
            if i=="+":
                ans.append(ans[len(ans)-1]+ans[len(ans)-2])
            elif i=="D":
                ans.append(2*(ans[len(ans)-1]))
            elif i=="C":
                ans.pop()
            else:
                ans.append(int(i))
        return sum(ans)