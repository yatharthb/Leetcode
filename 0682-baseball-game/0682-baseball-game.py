class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        
        for o in operations:
            if o == "+":
                if len(st) > 1:
                    st.append(st[-1]+st[-2])
                
                elif len(st) == 1:
                    st.append(st[-1])
                
                else:
                    continue;
            
            elif o == "C":
                if len(st) > 0:
                   st.pop()
                   continue;
                continue;
            
            elif o == "D":
               if len(st) > 0:
                   st.append(2*st[-1])
                   continue;
                
               continue;
            
            else:
                st.append(int(o))
        
        return sum(st)