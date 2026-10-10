class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            # If mid element is greater than the rightmost element,
            # the inflection point (minimum) must be to the right of mid.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, mid could be the minimum, or the minimum is to its left.
            else:
                r = mid
                
        return nums[l]
