#https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            if(target - num in dict):
                return [dict.get(target-num), index]
            dict[num] = index