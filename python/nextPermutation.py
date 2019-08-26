# https://leetcode.com/problems/next-permutation/submissions/
class Solution(object):
    def nextPermutation(self, nums):
        index = len(nums)-1
        # loop backwards from the end of the list
        while index>0:
            # find the neighbouring numbers that have the relation
            # where the left number decreases from the right number
            if nums[index]>nums[index-1]:
                j = len(nums)-1
                # starting from the right side again,
                # we iterate until we find the next biggest number
                while nums[j] <= nums[index-1]:
                    j-=1 
                # swap the number where the decrease relation occurs and
                # the next highest number we found
                self.swap(nums, index-1, j)
                break
            index-=1
        # finally, resort all numbers in ascending order from
        # number that we found the decrease relation to occur at
        # all the way until the end of the list of nums
        self.sort(nums, index)
        
    def sort(self,nums, start):
        i=start; j=len(nums)-1
        while i<j:
            self.swap(nums, i, j)
            i+=1
            j-=1
    
    def swap(self, nums, i, j):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp