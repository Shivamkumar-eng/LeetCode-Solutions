class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
            
        buckets = {}
        w = valueDiff + 1
        
        for i, x in enumerate(nums):
            m = x // w
            
            # 1. Direct hit in same bucket
            if m in buckets:
                return True
                
            # 2. Adjacent bucket checks
            if (m - 1 in buckets and x - buckets[m - 1] <= valueDiff) or \
               (m + 1 in buckets and buckets[m + 1] - x <= valueDiff):
                return True
                
            buckets[m] = x
            
            # 3. Maintain sliding window
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]
                
        return False