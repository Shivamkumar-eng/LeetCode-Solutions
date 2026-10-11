class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sm=0
        for i in range(1,len(nums)+1):
            if len(nums)%i==0:
                 sm+=nums[i-1]*nums[i-1]
        return sm