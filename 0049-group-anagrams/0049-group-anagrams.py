class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        rm = {}
        res = []
        
        ss = ""
        
        for s in strs:
            
            ss = ''.join(sorted(s))
            
            if ss in rm:
                res[rm[ss]].append(s)
            else:
                rm[ss] = len(res)
                res.append([s])
            
        
        return res
                
        
        