class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        l= len(nums1)
        # mid=int(l/2)
        # print(mid)
        # print(l/2)
        # print(l)
        # print(mid*2)

        if l%2==0:
            return((nums1[int(l/2)]+nums1[int(l/2)-1])/2)
        else: 
            return(nums1[int(l/2)])
