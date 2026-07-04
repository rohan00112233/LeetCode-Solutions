class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergearray= []
        mergearray = nums1 + nums2
        mergearray.sort()

        n = len(mergearray)
        mid = n//2
        if n%2 !=0 :
            return mergearray[mid]
        else:
            return (mergearray[mid - 1] + mergearray[mid])/2
      