// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// https://leetcode.com/problems/two-sum/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i=0;
        HashMap<Integer, Integer> map = new HashMap<>();
        while(!map.containsKey(target - nums[i])){
            map.put(nums[i], i);
            i++;
        }
        return new int[]{map.get(target-nums[i]), i};
    }
}