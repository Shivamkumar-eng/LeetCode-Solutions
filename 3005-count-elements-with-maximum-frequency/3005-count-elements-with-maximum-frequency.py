class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        max_freq = 0
        total_freq = 0
        
        for num in nums:
            # 1. Update frequency map without using .get()
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            
            freq = dic[num]
            
            # 2. Maintain max frequency and total sum in a single pass
            if freq > max_freq:
                max_freq = freq
                total_freq = freq        # Reset total to current max frequency
            elif freq == max_freq:
                total_freq += max_freq  # Add max frequency for tied elements
                
        return total_freq