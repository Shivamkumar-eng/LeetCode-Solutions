class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i , num in enumerate(nums):
            complement=target-num
            if complement in dic:
                return [i,dic[complement]]
            dic[num]=i