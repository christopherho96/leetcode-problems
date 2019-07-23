#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        current = nums[0]
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != current:
                nums[j] = nums[i]
                current = nums[i]
                j += 1
        return j