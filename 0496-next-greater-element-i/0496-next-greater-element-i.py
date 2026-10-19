class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        ans=[]
        d={}
        for i in range(len(nums2)-1,-1,-1):
            while len(stack)>0 and nums2[i]>stack[-1]:
                stack.pop()
            if not stack:
                d[nums2[i]]=-1
            else:
                d[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            ans.append(d[nums1[i]])
        return ans