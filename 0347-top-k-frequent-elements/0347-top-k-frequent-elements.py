import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}

        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        heap=[]
        for num,freq in d.items():
            heapq.heappush(heap,(freq,num))
        
            if len(heap)>k:
                heapq.heappop(heap)
        
        result=[]
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result

                
        
