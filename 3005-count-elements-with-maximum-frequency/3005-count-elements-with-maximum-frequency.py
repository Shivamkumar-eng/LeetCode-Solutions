class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        
        # Pass 1: Build frequency map
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        # Pass 2: Find the maximum frequency and sum all matching frequencies
        max_freq = 0
        total = 0
        
        for freq in dic.values():
            if freq > max_freq:
                max_freq = freq
                total = freq        # Reset total for the new maximum
            elif freq == max_freq:
                total += max_freq   # Accumulate total for matching max frequencies
                
        return total