class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        median=0
        mid=(len(nums1)+ len(nums2))
        if mid%2==0:
            median=(nums3[int(mid/2)]+nums3[int(mid/2)-1])/2
        else: 
            median=nums3[int(mid/2)]
        return median