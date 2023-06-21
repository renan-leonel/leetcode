class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS, hashmapT = {} , {}

        if len(s) != len(t): 
            return False

        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
            
        if hashmapS == hashmapT:
            return True
        return False