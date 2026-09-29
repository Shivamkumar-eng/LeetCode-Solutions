class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_map = {0: 1}
        
        for num in nums:
            current_sum += num
            target = current_sum - k
            
            # Check if target exists without .get()
            if target in prefix_map:
                count += prefix_map[target]
                
            # Update frequency without .get()
            if current_sum in prefix_map:
                prefix_map[current_sum] += 1
            else:
                prefix_map[current_sum] = 1
                
        return count