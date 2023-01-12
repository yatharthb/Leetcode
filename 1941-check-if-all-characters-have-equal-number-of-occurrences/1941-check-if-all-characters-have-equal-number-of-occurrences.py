class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        cmap = {}
        
        for c in s:
            if c not in cmap:
                cmap[c] = 1
            else:
                cmap[c] += 1
                
        
        return min(cmap.values()) == max(cmap.values())