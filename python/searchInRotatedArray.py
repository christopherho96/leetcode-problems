#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
# Hint: I know that if target is greater than the last number in the array,
# then I want to do binary search from 0 up to rotation index
# Oppositely, if its less then the target, then I want to binary search from 
# rotation point to last index in array
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        rot = self.findLowestValueIndex(nums)
        if target > nums[len(nums)-1]:
            return self.binarySearch(nums, 0, rot-1,target)
        else:
            return self.binarySearch(nums, rot, len(nums) - 1, target)
        
    def findLowestValueIndex(self, nums):
        lo=0; hi=len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if nums[mid]>nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
    def binarySearch(self, nums, left, right, target):
        middle = left + (right - left)//2
        if nums[middle] == target:
            return middle
        elif left>=right:
            return -1
        else:
            if target < nums[middle]:
                return self.binarySearch(nums, left, middle, target)
            else:
                return self.binarySearch(nums, middle + 1, right, target)