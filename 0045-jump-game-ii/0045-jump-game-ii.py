class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Loop up to the second-to-last element
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the current jump range, we must jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps