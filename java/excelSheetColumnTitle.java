// Given a positive integer, return its corresponding column title as appear in an Excel sheet.
// https://leetcode.com/problems/excel-sheet-column-title/

class Solution {
    public String convertToTitle(int n) {
        StringBuilder result = new StringBuilder();
        while(n>0){
            n--;
            result.insert(0, (char)('A' + n % 26));
            n /= 26;
        }
        return result.toString();
    }
}