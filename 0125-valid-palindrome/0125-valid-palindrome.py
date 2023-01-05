class Solution:
    def isPalindrome(self, s: str) -> bool:
        #96 32
        #print(ord(":"),ord(","))
        filteredString = ""
        validCharacters = set("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        
        for c in s:
            if c not in validCharacters:
                continue;
            
            if ord(c) > 96:
                filteredString += chr(ord(c)-32)
            
            else:
                filteredString += c
                
        
        return filteredString == filteredString[::-1]
                