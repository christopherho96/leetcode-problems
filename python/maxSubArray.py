# https://leetcode.com/problems/maximum-subarray/submissions/
class Solution(object):
    def maxSubArray(self, nums):
        currentMax = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
            currentMax = max(currentMax, nums[i])
        return currentMax
    
# We know that if the previous value is negative, then adding it to the 
# current num in the list will only decrease it. Therefore, if a previous 
# number is greater than 0, then we know it has the possibility to 
# increase the max, so we add it to the current number and save it.
# Then finally, we check if the new sum value has 
# become bigger then any previous max and save it