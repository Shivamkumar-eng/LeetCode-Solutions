class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
    
        merged = []
    
        for interval in intervals:
        # If merged is empty or no overlap, append current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # Overlap exists, merge intervals by extending the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
            
        return merged