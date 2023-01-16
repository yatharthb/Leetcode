class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        mx = arr[len(arr)-1]
        
        arr[len(arr)-1] = -1
        
        for i in range(len(arr)-2,-1,-1):
            
            if arr[i] > mx:
                arr[i],mx = mx,arr[i]
            
            else:
                arr[i] = mx
        
        return arr