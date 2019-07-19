// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Given a string, find the length of the longest substring without repeating characters.

class Solution {
    public int lengthOfLongestSubstring(String s) {
        String tmp = "";
        int max = 0;
        int i = 0;
        while(i<s.length()){
            char c = s.charAt(i);
            if(tmp.indexOf(c) != -1){
                tmp = tmp.substring(tmp.indexOf(c) + 1 , tmp.length());
            }
            tmp += c;
            max = Math.max(max, tmp.length());
            i++;
        }
        return max;
    }
}