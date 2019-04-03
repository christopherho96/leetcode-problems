// Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
// https://leetcode.com/problems/maximum-product-subarray/

class Solution {
    public int maxProduct(int[] nums) {
        // O(n2) runtime due to nested loops
        if (nums.length == 1) return nums[0];
        
        // int currentMax = nums[0];
        // for(int i=0; i< nums.length; i++){
        //     int tmp = nums[i];
        //     currentMax = Math.max(tmp, currentMax);
        //     for(int j=i+1; j<nums.length; j++){
        //         tmp *= nums[j];
        //         if(tmp >currentMax) currentMax = tmp;
        //     }
        // }
        // return currentMax;
        
        
        int max = nums[0];
        int min = nums[0];
        int result = nums[0];
        
        // O(n) run time, loops through entire array only once
        for(int i = 1; i< nums.length; i++){
            int tmp = max;
            max = Math.max(Math.max(max* nums[i], min *nums[i]), nums[i]);
            min = Math.min(Math.min(tmp*nums[i], min*nums[i]), nums[i]);
            
            if(max>result) result = max;
        }
        
        return result;
        
    }
}