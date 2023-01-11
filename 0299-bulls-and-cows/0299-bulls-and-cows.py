class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        cows = 0
        hs = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            elif secret[i] in hs:
                hs[secret[i]] += 1
            
            else:
                hs[secret[i]] = 1
                
        
        for i in range(len(guess)):
            if secret[i] != guess[i]:
                if  guess[i] not in hs:
                    continue;
                elif hs[guess[i]] < 1:
                    continue;
                
                else:
                    hs[guess[i]] -= 1
                    cows += 1
        
        res = str(bulls) + "A" + str(cows) + "B"
        return res
            