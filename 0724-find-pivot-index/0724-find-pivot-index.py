class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        m=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            m.append(sum)
        for j in range(len(nums)):
            if m[j]-nums[j]==m[-1]-m[j]:
                return j
        return -1