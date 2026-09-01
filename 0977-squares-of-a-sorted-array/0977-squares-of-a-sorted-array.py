class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        for i in range(len(nums)):
            nums[i]=abs(nums[i])**2
        nums=sorted(nums)
        return nums