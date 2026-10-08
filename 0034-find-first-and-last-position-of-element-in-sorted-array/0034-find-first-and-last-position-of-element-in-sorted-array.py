class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1,-1]
        l=0
        first=-1
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                    first=mid
                r=mid-1
            else:
                l=mid+1
        if first==-1:
            return [-1,-1]

        l,r= first,len(nums)-1
        last=first
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]<=target:
                if nums[mid]==target:
                    last=mid
                l=mid+1
            else:
                r=mid-1
        return[first,last]