class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            k -= 1
            
            temp = nums.pop()
            nums.insert(0,temp)