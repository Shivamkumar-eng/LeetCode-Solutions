class Solution:
    def canJump(self, nums: list[int]) -> bool:
        fartest=0
        for i in range(len(nums)):
            if i>fartest:
                return False
            if fartest<(i+nums[i]):
                fartest=i+nums[i]
        return True