#https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=programming-skills
def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        return len(l[len(l)-1])