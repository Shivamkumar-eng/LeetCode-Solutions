class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*101
        for i in nums:
            count[i]+=1
        
        running_time=0
        for i in range(101):
            temp=count[i]
            count[i]=running_time
            running_time+=temp
        return [count[num] for num in nums]