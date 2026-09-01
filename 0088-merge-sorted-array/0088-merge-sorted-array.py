class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return
        elif m==0 :
            nums1[:]=nums2
            return
        nums1[m:]=nums2
        nums1.sort()
        return nums1
        