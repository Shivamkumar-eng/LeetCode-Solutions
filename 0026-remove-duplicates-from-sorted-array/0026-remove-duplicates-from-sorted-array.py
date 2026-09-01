class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        List1 = []
        k=0
        for i in range(len(nums)):
            if nums[i] not in List1:
                List1.append(nums[i])
                k+=1
        nums[:k]=List1
        return k