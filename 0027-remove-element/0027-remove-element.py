class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for k in range(len(nums)):
            if nums[k]!=val:
                nums[i]=nums[k]
                i+=1
        return i