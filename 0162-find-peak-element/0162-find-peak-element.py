class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        maximum=float('-inf')
        index=0
        for i in range(len(nums)):
            if nums[i]>maximum:
                maximum=nums[i]
                index=i
        return index