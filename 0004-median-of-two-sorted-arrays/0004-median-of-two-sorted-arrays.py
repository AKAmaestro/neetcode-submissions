class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        mid=(len(nums1))
        if mid%2==0:
            return((nums1[int(mid/2)]+nums1[int(mid/2)-1])/2)
        else: 
            return(nums1[int(mid/2)])
