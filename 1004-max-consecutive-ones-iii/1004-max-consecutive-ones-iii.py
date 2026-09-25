class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            # If the current element is 0, increment zero counter
            if nums[right] == 0:
                zero_count += 1
            
            # Shrink window from the left if zeroes exceed allowed flips
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum valid window length
            max_length = max(max_length, right - left + 1)
            
        return max_length