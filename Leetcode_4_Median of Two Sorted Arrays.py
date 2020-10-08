class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median=0
        nums1.extend(nums2)
        nums1.sort()
        m = len(nums1)
        if m%2==0:
            n = int(m/2)
            median = (nums1[n]+nums1[n-1])/2
        else:
            median = nums1[m//2]
        return median
