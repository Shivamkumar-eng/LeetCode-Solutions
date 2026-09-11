class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        k = k % m
        if k == 0:
            return
            
        nums[:] = nums[-k:] + nums[:-k]