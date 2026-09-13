class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            
            # If the current number matches our candidate, we increment count.
            # Otherwise, we decrement count.
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate