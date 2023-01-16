class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        sp = 0
        tp = 0
        
        
        for tp in range(len(t)):
            if t[tp] == s[sp]:
                sp += 1
                
                if sp == len(s):
                    return True
                
                continue;
            
            else:
                continue;
        
        return False