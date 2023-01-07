class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        mx = 0  #this variable tracks the max distance from the nearest heater
        
        htr = 0 #this variable tracks the index of the nearest heater
        houses.sort()
        heaters.sort()
        for house in houses:
                if htr < len(heaters)-1:
                    while abs(house-heaters[htr]) >= abs(house-heaters[htr+1]):
                        #print(htr)
                        htr += 1
                        if htr == len(heaters)-1:

                            break;
                #print(house,htr)
                if htr < len(heaters) - 1:
                    mx = max(min(abs(house-heaters[htr]),abs(house-heaters[htr+1])),mx)
                else:
                    mx = max(abs(house-heaters[htr]),mx)
                
        return mx