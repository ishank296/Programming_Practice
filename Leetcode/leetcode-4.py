# Given two sorted arrays nums1 and nums2 of size m and n
# respectively, return the median of the two sorted arrays.
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = list()
        idx1, idx2 = 0, 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                merged.append(nums1[idx1])
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                merged.append(nums2[idx2])
                idx2 += 1
            else:
                merged.append(nums1[idx1])
                merged.append(nums2[idx2])
                idx1 += 1
                idx2 += 1
        if idx1 < len(nums1):
            merged += nums1[idx1:]
        if idx2 < len(nums2):
            merged += nums2[idx2:]
        if len(merged) % 2 == 0:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
        else:
            return merged[len(merged) // 2]

