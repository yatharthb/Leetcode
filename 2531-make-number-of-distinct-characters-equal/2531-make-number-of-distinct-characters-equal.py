class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        w1 = {}
        w2 = {}
        
        for c in word1:
            if c in w1:
                w1[c] += 1
            
            else:
                w1[c] = 1
                
        
        for d in word2:
            if d in w2:
                w2[d] += 1
            
            else:
                w2[d] = 1
        
        if abs(len(w1.keys()) - len(w2.keys())) == 0:
            #if len(w1.keys) > 1:
            if max(w1.values()) == 1 and min(w2.values()) > 1:
                for ds in w1:
                    if ds in w2:
                        return True
                return False
            if max(w2.values()) == 1 and min(w1.values()) > 1:
                for gs in w2:
                    if gs in w1:
                        return True
                return False
            #return min(len(word1),len(word2)) > 1
            return True
        
        if abs(len(w1.keys()) - len(w2.keys())) > 2:
            return False
        
        if abs(len(w1.keys()) - len(w2.keys())) == 1:
        
            if len(w1.keys()) > len(w2.keys()):
                if max(w2.values()) == 1:
                    for ww in w2:
                        if ww in w1:
                            for wa in w1:
                                if wa not in w2 and w1[wa] == 1:
                                   return True
                        
                    return False
                for wc in w1:
                    if w1[wc] > 1 and wc not in w2:
                        for wt in w2:
                            if w2[wt] > 1 and wt in w1:
                                return True
                    
                for wc in w1:
                    if w1[wc] == 1 and wc not in w2:
                        for wt in w2:
                            if w2[wt] > 1 and wt not in w1:
                                return True
                
                for wc in w1:
                    if w1[wc] == 1 and wc in w2:
                        for wt in w2:
                            if wt != wc and w2[wt] > 1 and wt in w1:
                                return True
                        
                return False
            
            elif len(w2.keys()) > len(w1.keys()):
                if max(w1.values()) == 1:
                    for wy in w1:
                        if wy in w2:
                            for wz in w2:
                                if wz not in w1 and w2[wz] == 1:
                                   return True
                    return False
                for wm in w2:
                    if w2[wm] > 1 and wm not in w1:
                        for wj in w1:
                            if w1[wj] > 1 and wj in w2:
                                return True
                for wm in w2:
                    if w2[wm] == 1 and wm not in w1:
                        for wj in w1:
                            if w1[wj] > 1 and wj not in w2:
                                return True
                for wm in w2:
                    if w2[wm] == 1 and wm in w1:
                        for wj in w1:
                            if wj != wm and w1[wj] > 1 and wj in w2:
                                return True
                return False
        if abs(len(w1.keys()) - len(w2.keys())) == 2:
            if len(w1.keys()) > len(w2.keys()):
                if max(w2.values()) == 1:
                    return False
                for wc in w1:
                    if w1[wc] == 1 and wc not in w2:
                        for wt in w2:
                            if w2[wt] > 1 and wt in w1:
                                return True
                        return False
                return False
            
            elif len(w2.keys()) > len(w1.keys()):
                if max(w1.values()) == 1:
                    return False
                for wm in w2:
                    if w2[wm] == 1 and wm not in w1:
                        for wj in w1:
                            if w1[wj] > 1 and wj in w2:
                                return True
                        return False
                return False
        
        