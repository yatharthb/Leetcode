class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        flag = False
        expected = ""
        prev = ""
        
        for i in range(len(s1)):
        
            if s1[i] != s2[i]:
                
                if flag == False:
                    if i > len(s1) - 2:
                       return False
                    flag = True
                    expected = s2[i]
                    prev = s1[i]
                
                elif flag == True:
                    if s1[i] == expected and s2[i] == prev:
                        return s1[i+1:] == s2[i+1:]
                    else:
                        return False
        if flag == True:
            return False
        return True