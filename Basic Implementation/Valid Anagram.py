#https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=programming-skills

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap=dict()
        for i in range(0,26):
            hashmap[chr(97+i)]=0
        
        for i in range(len(s)):
            hashmap[s[i]]+=1
        for i in range(len(t)):
            hashmap[t[i]]-=1    
        for keys in hashmap:
            if(hashmap[keys]!=0):
                return False
        return True