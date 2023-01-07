from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        pwrs = set()
        pwrs.add("1")
        i = 1
        while len(str(i)) < len(str(n))+2:
            i *=2
            pwrs.add(str(i))
        
        for p in [''.join(t) for t in permutations(str(n))]:
            
            if p in pwrs:
                return True
            
        return False
        
            
        
        
        