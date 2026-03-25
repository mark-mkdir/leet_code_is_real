class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp = nums1 + nums2
        temp = sorted(temp)
        if len(temp) % 2 == 0:
            result = temp[len(temp)//2] + temp[len(temp)//2 - 1]
            result = float(result) / 2
        else:
            result = temp[len(temp)//2]

        return result