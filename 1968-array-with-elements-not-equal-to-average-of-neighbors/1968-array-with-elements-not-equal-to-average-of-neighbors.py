class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        nl = len(nums)
        
        nums.sort()
        
        for i in range(nl//2):
            res.append(nums[i])
            res.append(nums[nl-1-i])
        
        if nums[(nl//2)+1] not in res:
            res.append(nums[(nl//2)+1])
        if nums[(nl - 1) - nl//2] not in res:
            res.append(nums[(nl - 1) - nl//2])
        
            
        return res
        
            