# https://leetcode.com/problems/single-number/submissions/
class Solution(object):
    def singleNumberDict(self, nums):
        #O(n) time complexoty with O(n) space complexity
        dict = {}
        for num in nums:
            if dict.get(num) == None:
                dict.update({num: 1})
            else:
                dict.pop(num)
        return dict.keys()[0]

    def singleNumberList(self, nums): 
        #O(nlogn) time complexity with O(1) space complexity
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]:
                i += 2
            else:
                break
        return nums[i]

print(Solution().singleNumberDict([2,2,1,5,7,6,7,6,5]))
print(Solution().singleNumberList([2,2,1,5,7,6,7,6,5]))