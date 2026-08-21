class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in s:
            if i in countS: 
                countS[i] +=1
            else:
                countS[i] = 1
        for i in t:
            if i in countT: 
                countT[i] +=1
            else:
                countT[i] = 1
        
        for key in countS:
            if countS[key] != countT.get(key,0):
                return False

        return True
        
    
        