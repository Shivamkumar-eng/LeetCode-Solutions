class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Replace non-positive numbers (<= 0) with n + 1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
                
        # Step 2: Mark present numbers by setting nums[val - 1] to negative
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                    
        # Step 3: First index with a POSITIVE value was never marked
        for i in range(1, n + 1):
            if nums[i - 1] > 0:
                return i
                
        return n + 1