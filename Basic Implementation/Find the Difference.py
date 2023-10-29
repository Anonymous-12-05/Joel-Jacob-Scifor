#https://leetcode.com/problems/find-the-difference/description/?envType=study-plan-v2&envId=programming-skills
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap=dict()
        s.lower()
        t.lower()
        ans=""
        for i in range(0,26):
            hashmap[chr(97+i)]=0
        #for keys in hashmap:
        #    print(keys,hashmap[keys])

        for i in range(len(s)):
            hashmap[s[i]]+=1
        for i in range(len(t)):
            hashmap[t[i]]+=1
        for keys in hashmap:
            if(hashmap[keys]%2!=0):
                ans=keys
        return ans
             