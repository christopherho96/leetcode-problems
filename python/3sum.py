#https://leetcode.com/problems/3sum/submissions/
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = []
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    answer.append(triplet)
                    while l<r and nums[l+1] == nums[l]:
                        l+=1
                    while l< r and nums[r] == nums[r-1]:
                        r-=1
                    l +=1; r-=1                    
                elif sum < 0:
                    l += 1
                else: 
                    r -= 1
        return answer
        