class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sm=0
        n=len(nums)
        for i in range(1,n+1):
            if n%i==0:
                 sm+=nums[i-1]**2
        return sm