class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i ,num in enumerate(nums):
            if num in dic:
                dic[num]=dic[num]+1
            else:
                
                dic[num]=1
        max=0
        for j in range(len(nums)):
            if dic[nums[j]]>max:
                max=dic[nums[j]]
                k=j
        return nums[k]