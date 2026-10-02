class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = 2
        for r in range(2, len(nums)):
            if nums[r] != nums[i - 2]:
                nums[i] = nums[r]
                i += 1
        return i
