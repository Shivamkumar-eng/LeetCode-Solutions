class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        d={}
        for i in range(len(numbers)):
            complement=target-numbers[i]
            if complement in d:
                return [d[complement],i+1]
            d[numbers[i]]=i+1