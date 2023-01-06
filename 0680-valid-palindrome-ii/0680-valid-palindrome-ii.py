class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        reversedString = s[::-1]
        #abcddecba
        #abceddcba
        for i in range(len(s)//2):
            
            if s[i] == reversedString[i]:
                continue;
            
            else:
                
                ns = s[:i] + s[i+1:]
                ns2 = reversedString[:i] + reversedString[i+1:]
                
                if ns == ns[::-1] or ns2 ==ns2[::-1]:
                    return True
                return False
            
            
        
        return True