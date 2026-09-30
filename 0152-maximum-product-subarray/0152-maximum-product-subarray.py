class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Initialize tracking variables with the first element
        current_max = nums[0]
        current_min = nums[0]
        global_max = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If the current number is negative, max and min swap roles
            # because a negative multiplied by a minimum (negative) becomes a maximum
            if num < 0:
                current_max, current_min = current_min, current_max
            
            # Decide whether to start a new subarray at 'num' or continue the existing one
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            # Update the highest product found anywhere so far
            global_max = max(global_max, current_max)
            
        return global_max
