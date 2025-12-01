# AnaGram
# https://leetcode.com/problems/valid-anagram/  
class Solution:
    s ="anagram" 
    t ="nagaram"
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        countS, CountT = {},{}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[1],0)
            countT[t[i]] = 1 + countT.get(t[1],0)
        for c in countS:
            if countS[c]!=counT.get(c,0):
                return False
            return Ture 