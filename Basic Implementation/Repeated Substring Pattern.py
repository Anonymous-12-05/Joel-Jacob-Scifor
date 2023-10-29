#https://leetcode.com/problems/repeated-substring-pattern/description/?envType=study-plan-v2&envId=programming-skills

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        dummy=s+s

        dummy=dummy[1:len(dummy)-1]

        if s in dummy:
            return True
        else:
            return False