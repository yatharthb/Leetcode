class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        nextHighMap = {} #stores the indexes of previously encountered "next highest" values for temperatures
        
        
        for i,t in enumerate(temperatures):
            if i == len(temperatures) - 1:
                res.append(0)
                break;
            if (t in nextHighMap and nextHighMap[t] > i) or (t in nextHighMap and nextHighMap[t] == 0) :
                res.append(max(0,nextHighMap[t]-i))
            else:
                for j in range(i+1,len(temperatures)):
                    
                    if temperatures[j] > t:
                        nextHighMap[t] = j
                        res.append(j-i)
                        break;
                if (j == len(temperatures) - 1) and t >= temperatures[-1]:
                    nextHighMap[t] = 0
                    #print(i,t)
                    res.append(0)
        
        
        return res