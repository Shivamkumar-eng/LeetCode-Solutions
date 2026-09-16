class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                # Exact match found
                if current_sum == target:
                    return target
                
                # Update closest sum if current is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                # Move pointers based on comparison with target
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum