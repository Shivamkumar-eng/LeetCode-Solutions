class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
        
        # Step 1: Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize merged list with the first interval
        merged = [intervals[0]]
        
        # Step 3: Iterate through the rest
        for current in intervals[1:]:
            last_merged = merged[-1]
            
            # Step 4 & 5: Check for overlap
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)
                
        return merged