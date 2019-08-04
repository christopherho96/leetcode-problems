#https://leetcode.com/problems/merge-sorted-array/submissions/
# run O(m+n) time
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = n; j = 0; k = 0
        nums1[n:] = nums1[:m]
        while k < m+n and i<m+n and j<n:
            nums1[k] = min(nums1[i], nums2[j])
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                j += 1
            k += 1
        
        if i == m+n:
            nums1[k:] = nums2[j:]
        if j == n:
            nums1[k:] = nums1[i:]
            
        return nums1