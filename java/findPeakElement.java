// A peak element is an element that is greater than its neighbors.

// Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

// https://leetcode.com/problems/find-peak-element/

class Solution {
    int index = 0;
    public int findPeakElement(int[] nums) {
        
        if(nums.length>1)
            if(nums[nums.length-1]>nums[nums.length-2]) return nums.length -1;
        
        // binary search using recursion
        divideAndConquer(nums, 0, nums.length);
        
        return index;
    }
    
    private void divideAndConquer(int[] nums, int start, int end){
        if(end-start < 2 || index != 0) return;
        
        int mid = (start + end)/2;
        divideAndConquer(nums, start, mid);
        divideAndConquer(nums, mid, end);
        
        isPeak(nums, start, mid, end);
    }  
    
    private void isPeak(int[] nums, int start, int mid, int end){
        if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1]) 
            index = mid;
    }
}