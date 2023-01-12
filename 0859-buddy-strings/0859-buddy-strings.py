class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        flag = False
        rep = False
        expected = ""
        prev = ""
        chars = set()
        if len(s) != len(goal):
            return False
        
        
        for i in range(len(s)):
            if s[i] not in chars:
                chars.add(s[i])
            else:
                rep = True
            if s[i] != goal[i]:
                
                if flag == False:
                    if i > len(s) - 2:
                       return False
                    flag = True
                    expected = goal[i]
                    prev = s[i]
                
                elif flag == True:
                    if s[i] == expected and goal[i] == prev:
                        return s[i+1:] == goal[i+1:]
                    else:
                        return False
        if flag == True:
            return False
        return rep